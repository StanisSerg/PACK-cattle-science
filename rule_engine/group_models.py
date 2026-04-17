"""
group_models.py — модели для Group-Level Rule Engine

Отвечает на вопрос: "система в порядке или сломана?"
Не трогает cow-level models.py
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any
import yaml


@dataclass
class GroupPrediction:
    """Прогноз на уровне группы"""
    primary_metric: str | None = None
    target_value: str | None = None
    timeframe: str | None = None
    confidence: str | None = None
    secondary_metrics: list[str] = field(default_factory=list)


@dataclass
class GroupDecision:
    """Решение на уровне группы"""
    rule: str | None = None
    mode: str = "group"
    severity: str | None = None  # emergency / critical / high / medium / low / normal
    confidence: str | None = None
    verdict: str | None = None
    label: str | None = None  # человекочитаемое, например GROUP_TRANSITION_CRISIS
    action: str | None = None
    strategy: dict[str, Any] = field(default_factory=dict)
    reasoning: list[str] = field(default_factory=list)
    basis: dict[str, Any] = field(default_factory=dict)


@dataclass
class GroupEvaluation:
    """Оценка исполнения стратегии"""
    status: str | None = None  # success / partial / failure / pending
    delta: dict[str, Any] = field(default_factory=dict)
    notes: str | None = None


def load_yaml(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping/dict")
    return data


def save_yaml(path: str, data: dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def attach_derived_group(case: dict[str, Any]) -> None:
    """
    Рассчитать derived_group параметры из group/metrics/raw.
    Это сердце Group Engine — здесь сырые данные превращаются в флаги для правил.
    """
    group = case.get("group", {})
    metrics = case.get("metrics", {})
    raw = case.get("raw", {})
    derived = case.setdefault("derived_group", {})

    n_total = group.get("n_total", 0)
    n_tested = group.get("n_tested", 0)
    n_at_risk = group.get("n_at_risk", 0)

    # --- Milk signals ---
    milk = metrics.get("milk", {})
    mean_deviation = milk.get("mean_deviation_pct")
    if isinstance(mean_deviation, (int, float)):
        derived["milk_deviation_flag"] = mean_deviation < -15
        derived["milk_critical_flag"] = mean_deviation < -25
    else:
        derived["milk_deviation_flag"] = False
        derived["milk_critical_flag"] = False

    # --- Metabolic signals ---
    metab = metrics.get("metabolic", {})
    prevalence_bhb = metab.get("prevalence_bhb_gt_1_2", 0)
    prevalence_ca = metab.get("prevalence_ca_lt_2_0", 0)
    prevalence_fever = metab.get("prevalence_fever", 0)

    derived["metabolic_cluster_flag"] = (
        prevalence_bhb >= 25 or prevalence_ca >= 25 or prevalence_fever >= 25
    )
    derived["metabolic_critical_flag"] = (
        prevalence_bhb >= 50 or prevalence_ca >= 50 or prevalence_fever >= 50
    )

    # --- Prevalence / coverage ---
    tested_ratio = n_tested / n_total if n_total > 0 else 0.0
    derived["high_prevalence_flag"] = (n_at_risk / n_total >= 0.5) if n_total > 0 else False
    derived["adequate_test_coverage"] = tested_ratio >= 0.8

    # --- Composite group health index ---
    # Очень простой индекс: 0-100, где 0 = всё хорошо, 100 = катастрофа
    score = 0
    if derived["milk_deviation_flag"]:
        score += 30
    if derived["milk_critical_flag"]:
        score += 20
    if derived["metabolic_cluster_flag"]:
        score += 25
    if derived["metabolic_critical_flag"]:
        score += 15
    if derived["high_prevalence_flag"]:
        score += 10
    derived["group_health_index"] = min(score, 100)

    # --- Transition-specific ---
    dim_range = group.get("dim_range", "")
    derived["is_transition_group"] = "0-" in str(dim_range) or "21" in str(dim_range)


# Разрешённые статусы исполнения
EXECUTION_STATUSES = {"planned", "in_progress", "done", "skipped", "blocked"}


def _get_strategy(case: dict[str, Any]) -> dict[str, Any]:
    """Извлечь strategy из group_decision или group_rule_results."""
    gd = case.get("group_decision", {})
    strategy = gd.get("basis", {}).get("strategy") or {}
    if not strategy:
        for rr in case.get("group_rule_results", []):
            dec = rr.get("decision", {})
            if dec.get("strategy"):
                strategy = dec["strategy"]
                break
    return strategy


def init_execution_from_strategy(case: dict[str, Any]) -> None:
    """
    Создать блок execution на основе strategy.
    Вызывается сразу после run_group_case.py
    """
    strategy = _get_strategy(case)
    actions = strategy.get("actions", [])
    execution = case.setdefault("execution", {})
    execution["actions"] = []
    for a in actions:
        execution["actions"].append({
            "id": a["id"],
            "mandatory": a.get("mandatory", True),
            "status": "planned",
            "started_at": None,
            "completed_at": None,
            "notes": None,
        })
    execution["summary"] = compute_execution_summary(execution)
    execution["last_updated"] = None


def compute_execution_summary(execution: dict[str, Any]) -> dict[str, Any]:
    """Посчитать execution_summary из блока execution."""
    actions = execution.get("actions", [])
    mandatory_total = sum(1 for a in actions if a.get("mandatory", True))
    done = sum(1 for a in actions if a.get("mandatory", True) and a.get("status") == "done")
    in_progress = sum(1 for a in actions if a.get("mandatory", True) and a.get("status") == "in_progress")
    missing = sum(1 for a in actions if a.get("mandatory", True) and a.get("status") in ("planned", "blocked"))
    incomplete_ids = [
        a["id"] for a in actions
        if a.get("mandatory", True) and a.get("status") not in ("done", "skipped")
    ]
    return {
        "mandatory_total": mandatory_total,
        "mandatory_done": done,
        "mandatory_in_progress": in_progress,
        "mandatory_missing": missing,
        "execution_complete": len(incomplete_ids) == 0,
        "incomplete_action_ids": sorted(incomplete_ids),
    }


def update_execution_action(
    case: dict[str, Any],
    action_id: str,
    status: str,
    notes: str | None = None,
) -> None:
    """Обновить статус одного действия в execution."""
    if status not in EXECUTION_STATUSES:
        raise ValueError(f"Invalid execution status: {status!r}. Allowed: {EXECUTION_STATUSES}")
    execution = case.setdefault("execution", {})
    actions = execution.setdefault("actions", [])
    for a in actions:
        if a.get("id") == action_id:
            a["status"] = status
            if status == "in_progress" and a.get("started_at") is None:
                a["started_at"] = datetime.now(timezone.utc).isoformat()
            if status in ("done", "skipped"):
                a["completed_at"] = datetime.now(timezone.utc).isoformat()
            if notes is not None:
                a["notes"] = notes
            break
    else:
        raise ValueError(f"Action {action_id!r} not found in execution")
    execution["summary"] = compute_execution_summary(execution)
    execution["last_updated"] = datetime.now(timezone.utc).isoformat()


def dataclass_to_dict(obj: Any) -> dict[str, Any]:
    return asdict(obj)
