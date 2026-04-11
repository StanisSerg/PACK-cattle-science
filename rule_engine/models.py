"""
Модели данных для rule engine
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Any
import yaml


@dataclass
class Prediction:
    """Предсказание результата"""
    direction: dict[str, str] = field(default_factory=dict)
    range: dict[str, Any] = field(default_factory=dict)
    timeframe: str | None = None
    confidence: str | None = None


@dataclass
class Decision:
    """Решение rule engine"""
    triggered_rules: list[str] = field(default_factory=list)
    verdicts: list[str] = field(default_factory=list)
    primary_rule: str | None = None
    action: str | None = None
    reasoning: list[str] = field(default_factory=list)
    basis: dict[str, Any] = field(default_factory=dict)


@dataclass
class Evaluation:
    """Оценка результата (prediction vs fact)"""
    status: str | None = None  # success / partial / failure
    delta: dict[str, Any] = field(default_factory=dict)
    error_type: str | None = None
    root_cause: str | None = None
    notes: str | None = None


def load_yaml(path: str) -> dict[str, Any]:
    """Загрузить кейс из YAML"""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping/dict")
    return data


def save_yaml(path: str, data: dict[str, Any]) -> None:
    """Сохранить кейс в YAML"""
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )


def attach_derived(case: dict[str, Any]) -> None:
    """Рассчитать derived параметры из input"""
    input_data = case.setdefault("input", {})
    derived = case.setdefault("derived", {})

    # DMI ratio
    dmi_actual = input_data.get("dmi_actual")
    dmi_norm = input_data.get("dmi_norm")
    if isinstance(dmi_actual, (int, float)) and isinstance(dmi_norm, (int, float)) and dmi_norm > 0:
        derived["dmi_ratio"] = round(dmi_actual / dmi_norm, 3)

    # BCS loss
    bcs_at_calving = input_data.get("bcs_at_calving")
    bcs_current = input_data.get("bcs_current")
    if isinstance(bcs_at_calving, (int, float)) and isinstance(bcs_current, (int, float)):
        derived["bcs_loss"] = round(bcs_at_calving - bcs_current, 3)


def dataclass_to_dict(obj: Any) -> dict[str, Any]:
    """Конвертировать dataclass в dict"""
    return asdict(obj)
