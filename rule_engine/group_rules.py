"""
group_rules.py — групповые адаптации cow-level правил

Логика: читает derived_group, решает — система сломана или нет.
"""
from __future__ import annotations

from group_models import GroupDecision, GroupPrediction


class Rule001Group:
    """
    RULE-001G: Systemic Metabolic Deficit (Group Mode)

    Срабатывает когда в группе свежих коров кластерное нарушение метаболизма.
    """

    def evaluate(self, case: dict) -> tuple[GroupDecision | None, GroupPrediction | None]:
        derived = case.get("derived_group", {})
        group = case.get("group", {})
        metrics = case.get("metrics", {})

        # Применимость: только если группа в transition ИЛИ есть метаболический кластер
        is_transition = derived.get("is_transition_group", False)
        has_cluster = derived.get("metabolic_cluster_flag", False)

        if not (is_transition or has_cluster):
            return None, None

        ghi = derived.get("group_health_index", 0)
        milk_crit = derived.get("milk_critical_flag", False)
        metab_crit = derived.get("metabolic_critical_flag", False)
        high_prev = derived.get("high_prevalence_flag", False)
        milk_dev = derived.get("milk_deviation_flag", False)

        reasoning = []
        if is_transition:
            reasoning.append("is_transition_group_true")
        if has_cluster:
            reasoning.append("metabolic_cluster_detected")
        if milk_crit:
            reasoning.append("milk_deviation_critical")
        if metab_crit:
            reasoning.append("metabolic_flags_critical")
        if high_prev:
            reasoning.append("high_prevalence_at_risk")

        # --- Вердикт ---
        if ghi >= 80 or (milk_crit and metab_crit):
            severity = "critical"
            verdict = "RULE_001G_GROUP_TRANSITION_CRISIS"
            label = "GROUP_TRANSITION_CRISIS"
            action = "SYSTEMIC_INTERVENTION_MANDATORY"
            confidence = "high"
            strategy = {
                "id": "TRANSITION_CRISIS_V1",
                "label": "Кризис транзитного периода",
                "actions": [
                    {
                        "id": "FULL_VET_CHECK",
                        "type": "diagnostic",
                        "scope": "group",
                        "target": "all_transition_cows",
                        "mandatory": True,
                    },
                    {
                        "id": "RATION_CORRECTION",
                        "type": "system",
                        "domain": "nutrition",
                        "scope": "group",
                        "mandatory": True,
                    },
                    {
                        "id": "TEMP_MONITORING",
                        "type": "monitoring",
                        "scope": "group",
                        "frequency": "daily",
                        "duration_days": 14,
                        "mandatory": True,
                    },
                    {
                        "id": "SELECTIVE_PG",
                        "type": "treatment",
                        "scope": "individual",
                        "selection_rule": "bhb >= 1.2 AND (dmi_ratio < 0.8 OR anorexia_hours > 12)",
                        "mandatory": False,
                    },
                ],
                "constraints": {
                    "individual_override": False,
                    "rationale": "systemic_crisis_detected_local_decisions_prohibited",
                },
                "success_criteria": [
                    {
                        "metric": "bhb_prevalence_gt_1_2",
                        "target": "<25%",
                        "timeframe": "7-10 days",
                    },
                    {
                        "metric": "milk_deviation_mean",
                        "target": "> -15%",
                        "timeframe": "14 days",
                    },
                ],
            }
        elif metab_crit or high_prev or (milk_crit and milk_dev):
            severity = "high"
            verdict = "RULE_001G_HIGH_RISK"
            label = "GROUP_METABOLIC_HIGH_RISK"
            action = "SYSTEMIC_INTERVENTION_REQUIRED"
            confidence = "high"
            strategy = {
                "id": "TRANSITION_HIGH_RISK_V1",
                "label": "Высокий метаболический риск группы",
                "actions": [
                    {
                        "id": "RATION_REVIEW",
                        "type": "system",
                        "domain": "nutrition",
                        "scope": "group",
                        "mandatory": True,
                    },
                    {
                        "id": "BHB_SCREENING",
                        "type": "diagnostic",
                        "scope": "group",
                        "target": "all_fresh_cows_dim_lt_21",
                        "mandatory": True,
                    },
                    {
                        "id": "SELECTIVE_PG",
                        "type": "treatment",
                        "scope": "individual",
                        "selection_rule": "bhb >= 1.2",
                        "mandatory": False,
                    },
                ],
                "constraints": {
                    "individual_override": True,
                    "rationale": "high_risk_but_not_crisis_individual_decisions_allowed",
                },
                "success_criteria": [
                    {
                        "metric": "bhb_prevalence_gt_1_2",
                        "target": "<25%",
                        "timeframe": "10 days",
                    },
                    {
                        "metric": "group_health_index",
                        "target": "<60",
                        "timeframe": "10 days",
                    },
                ],
            }
        elif has_cluster or milk_dev:
            severity = "medium"
            verdict = "RULE_001G_MEDIUM_RISK"
            label = "GROUP_METABOLIC_ELEVATED"
            action = "ADJUST_RATION_AND_MONITOR"
            confidence = "medium"
            strategy = {
                "id": "TRANSITION_ELEVATED_V1",
                "label": "Повышенный метаболический фон группы",
                "actions": [
                    {
                        "id": "RATION_ADJUST",
                        "type": "system",
                        "domain": "nutrition",
                        "scope": "group",
                        "mandatory": False,
                    },
                    {
                        "id": "BHB_SPOT_CHECK",
                        "type": "diagnostic",
                        "scope": "group",
                        "target": "boundary_cases",
                        "mandatory": False,
                    },
                ],
                "constraints": {
                    "individual_override": True,
                    "rationale": "elevated_metabolic_background_monitor_and_adjust",
                },
                "success_criteria": [
                    {
                        "metric": "milk_deviation_mean",
                        "target": "> -10%",
                        "timeframe": "14 days",
                    },
                ],
            }
        else:
            severity = "low"
            verdict = "RULE_001G_MONITOR"
            label = "GROUP_WITHIN_NORMAL"
            action = "CONTINUE_ROUTINE_MONITORING"
            confidence = "medium"
            strategy = {
                "id": "TRANSITION_NORMAL_V1",
                "label": "Транзитный период в норме",
                "actions": [
                    {
                        "id": "ROUTINE_MONITORING",
                        "type": "monitoring",
                        "scope": "group",
                        "frequency": "weekly",
                        "mandatory": False,
                    },
                ],
                "constraints": {
                    "individual_override": True,
                    "rationale": "normal_group_standard_protocols_apply",
                },
                "success_criteria": [],
            }

        decision = GroupDecision(
            rule="RULE-001G",
            mode="group",
            severity=severity,
            confidence=confidence,
            verdict=verdict,
            label=label,
            action=action,
            strategy=strategy,
            reasoning=reasoning,
            basis={
                "group_health_index": ghi,
                "is_transition_group": is_transition,
                "metabolic_cluster_flag": has_cluster,
                "milk_critical_flag": milk_crit,
                "metabolic_critical_flag": metab_crit,
                "high_prevalence_flag": high_prev,
            },
        )

        prediction = GroupPrediction(
            primary_metric="bhb_prevalence_gt_1_2",
            target_value="< 25%",
            timeframe="7-10 days",
            confidence=confidence,
            secondary_metrics=["milk_deviation_mean", "group_health_index"],
        )

        return decision, prediction


# Инстанции правил для импорта
rule_001g = Rule001Group()
