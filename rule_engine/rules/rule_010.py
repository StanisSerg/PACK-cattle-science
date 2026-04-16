"""
RULE-010: Culling-Decision-Support
Economic threshold rule for culling based on metabolic, reproductive, and production risks
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-010"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-010.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    dim = input_data.get("dim")
    parity = input_data.get("parity") if input_data.get("parity") is not None else case.get("parity")
    pregnancy_status = input_data.get("pregnancy_status")
    expected_305d_yield = input_data.get("expected_305d_yield", 0)
    recent_purchase = input_data.get("recent_purchase", False)
    embryo_transfer = input_data.get("embryo_transfer", False)

    milk_yield_current = input_data.get("milk_yield_current")
    milk_yield_expected = input_data.get("milk_yield_expected")
    days_open = input_data.get("days_open", 0)
    treatment_cost_90d = input_data.get("treatment_cost_90d", 0)
    metabolic_issues_count = input_data.get("metabolic_issues_count", 0)
    reproductive_failures_count = input_data.get("reproductive_failures_count", 0)
    mastitis_cases_90d = input_data.get("mastitis_cases_90d", 0)
    locomotion_score = input_data.get("locomotion_score")
    heifer_available = input_data.get("heifer_available", False)
    genetic_value = input_data.get("genetic_value")

    # BLOCKING: pregnant high-value cow
    if pregnancy_status == "pregnant" and isinstance(expected_305d_yield, (int, float)) and expected_305d_yield > 9000:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_010_BLOCKED"],
            primary_rule=RULE_ID,
            action="DO_NOT_CULL_UNLESS_EMERGENCY",
            reasoning=["pregnant_high_value_cow"],
            basis={"rule": RULE_ID, "conditions": {"expected_305d_yield": expected_305d_yield}},
        )
        return decision, None

    # BLOCKING: recent purchase or ET
    if recent_purchase or embryo_transfer:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_010_BLOCKED"],
            primary_rule=RULE_ID,
            action="REQUIRES_INDIVIDUAL_ECONOMIC_REVIEW",
            reasoning=["recent_purchase_or_embryo_transfer"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(dim, int):
        return None, None

    # NOT APPLICABLE for dry cows (dim < 0 loosely, but here we use a flag if present)
    is_lactating = input_data.get("is_lactating", True)
    if not is_lactating:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_010_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="USE_DRY_COW_CULLING_PROTOCOL",
            reasoning=["dry_cow_different_economics"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # HARD: persistent problem
    persistent_problem = (
        metabolic_issues_count >= 2
        or reproductive_failures_count >= 2
        or mastitis_cases_90d >= 3
        or (isinstance(locomotion_score, (int, float)) and locomotion_score >= 3)
    )

    if not persistent_problem:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_010_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="CONTINUE_NORMAL_MANAGEMENT",
            reasoning=["no_persistent_problems_identified"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # SOFT conditions
    soft_multiple = sum([
        metabolic_issues_count >= 1,
        reproductive_failures_count >= 1,
        mastitis_cases_90d >= 1,
        isinstance(locomotion_score, (int, float)) and locomotion_score >= 2,
    ]) >= 2
    soft_days_open = isinstance(days_open, (int, float)) and days_open > 150
    soft_low_prod = (
        isinstance(milk_yield_current, (int, float))
        and isinstance(milk_yield_expected, (int, float))
        and milk_yield_expected > 0
        and (milk_yield_current / milk_yield_expected) < 0.70
    )
    soft_high_cost = isinstance(treatment_cost_90d, (int, float)) and treatment_cost_90d > 15000
    soft_late_lactation = isinstance(dim, int) and dim > 250
    soft_replacement = bool(heifer_available)
    soft_low_genetic = isinstance(genetic_value, (int, float)) and genetic_value < 0

    soft_score = sum([soft_multiple, soft_days_open, soft_low_prod, soft_high_cost, soft_late_lactation, soft_replacement, soft_low_genetic])

    if soft_score >= 4:
        verdict = "RULE_010_CULL_RECOMMENDED_HIGH"
        action = "CULL_ECONOMICALLY_JUSTIFIED"
        confidence = "HIGH"
    elif soft_score >= 2:
        verdict = "RULE_010_CULL_RECOMMENDED_MEDIUM"
        action = "CONSIDER_CULL_REVIEW_IN_30_DAYS"
        confidence = "MEDIUM"
    elif soft_score == 1:
        verdict = "RULE_010_CULL_RECOMMENDED_LOW"
        action = "MONITOR_60_DAYS"
        confidence = "LOW"
    else:
        verdict = "RULE_010_MONITOR_CLOSELY"
        action = "TRACK_METRICS_REASSESS_NEXT_CHECK"
        confidence = "LOW"

    reasoning = ["persistent_problem_identified"]
    if metabolic_issues_count >= 2:
        reasoning.append(f"metabolic_issues_{metabolic_issues_count}")
    if reproductive_failures_count >= 2:
        reasoning.append(f"reproductive_failures_{reproductive_failures_count}")
    if mastitis_cases_90d >= 3:
        reasoning.append(f"mastitis_cases_{mastitis_cases_90d}")
    if isinstance(locomotion_score, (int, float)) and locomotion_score >= 3:
        reasoning.append(f"chronic_lameness_ls_{locomotion_score}")

    if soft_multiple:
        reasoning.append("multiple_concurrent_issues")
    if soft_days_open:
        reasoning.append(f"days_open_{days_open}")
    if soft_low_prod:
        reasoning.append(f"low_production_{round((milk_yield_current / milk_yield_expected) * 100, 0)}%_of_expected")
    if soft_high_cost:
        reasoning.append(f"high_treatment_cost_{treatment_cost_90d}")
    if soft_late_lactation:
        reasoning.append(f"late_lactation_dim_{dim}")
    if soft_replacement:
        reasoning.append("replacement_heifer_available")
    if soft_low_genetic:
        reasoning.append("low_genetic_value")

    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=[verdict],
        primary_rule=RULE_ID,
        action=action,
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "dim": dim,
                "parity": parity,
                "metabolic_issues_count": metabolic_issues_count,
                "reproductive_failures_count": reproductive_failures_count,
                "mastitis_cases_90d": mastitis_cases_90d,
                "locomotion_score": locomotion_score,
                "days_open": days_open,
                "milk_yield_current": milk_yield_current,
                "milk_yield_expected": milk_yield_expected,
                "treatment_cost_90d": treatment_cost_90d,
                "heifer_available": heifer_available,
                "genetic_value": genetic_value,
            },
        },
    )

    prediction = Prediction(
        direction={
            "future_profitability": "negative_without_intervention" if soft_score >= 3 else "uncertain",
            "replacement_roi": "positive" if soft_replacement else "depends_on_availability",
        },
        range={
            "expected_annual_loss": [10000, 50000] if soft_score >= 4 else [0, 20000],
        },
        timeframe="12 months",
        confidence=confidence.lower(),
    )

    return decision, prediction
