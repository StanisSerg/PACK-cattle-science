"""
RULE-009: Lameness-Early-Detection
Early welfare and production screening based on locomotion score, BCS, bedding, and hoof health
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-009"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-009.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    locomotion_score = input_data.get("locomotion_score")
    bcs = input_data.get("bcs")
    bedding_score = input_data.get("bedding_score")
    surface_type = input_data.get("surface_type", "concrete")
    milk_yield_current = input_data.get("milk_yield_current")
    milk_yield_expected = input_data.get("milk_yield_expected")
    days_since_last_trim = input_data.get("days_since_last_trim")
    visible_lesions = input_data.get("visible_lesions", False)
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    # BLOCKING: non-ambulatory or severe injury
    severe_injury = {"fracture", "septic_arthritis", "deep_digital_sepsis", "non_ambulatory"}
    if severe_injury.intersection(set(clinical_signs)):
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_009_BLOCKED"],
            primary_rule=RULE_ID,
            action="REFER_TO_VETERINARY_EMERGENCY_PROTOCOL",
            reasoning=["non_ambulatory_or_severe_injury"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(locomotion_score, (int, float)):
        return None, None

    if locomotion_score < 2:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_009_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="CONTINUE_ROUTINE_LAMENESS_MONITORING",
            reasoning=["locomotion_score_normal"],
            basis={"rule": RULE_ID, "conditions": {"locomotion_score": locomotion_score}},
        )
        return decision, None

    # SOFT conditions
    soft_severe = locomotion_score >= 3
    soft_thin = isinstance(bcs, (int, float)) and bcs < 2.75
    soft_bedding = isinstance(bedding_score, (int, float)) and bedding_score < 2
    soft_surface = str(surface_type).lower() == "concrete" and not input_data.get("rubber_mats", False)
    soft_milk = (
        isinstance(milk_yield_current, (int, float))
        and isinstance(milk_yield_expected, (int, float))
        and milk_yield_expected > 0
        and (milk_yield_current - milk_yield_expected) / milk_yield_expected < -0.05
    )
    soft_trim = isinstance(days_since_last_trim, (int, float)) and days_since_last_trim > 60
    soft_lesions = bool(visible_lesions)

    soft_score = sum([soft_severe, soft_thin, soft_bedding, soft_surface, soft_milk, soft_trim, soft_lesions])

    if locomotion_score >= 3 and soft_score >= 2:
        verdict = "RULE_009_HIGH_RISK"
        action = "IMMEDIATE_HOOF_CARE_+_ENVIRONMENT_FIX"
        confidence = "HIGH"
    elif soft_score >= 2:
        verdict = "RULE_009_MEDIUM_RISK"
        action = "SCHEDULED_HOOF_CARE_+_ENVIRONMENT_REVIEW"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_009_LOW_RISK"
        action = "MONITOR_+_ROUTINE_TRIM_SCHEDULING"
        confidence = "LOW"

    reasoning = [f"locomotion_score_{locomotion_score}"]
    if soft_severe:
        reasoning.append("severely_lame")
    if soft_thin:
        reasoning.append(f"bcs_{bcs}_<_2.75")
    if soft_bedding:
        reasoning.append("poor_bedding")
    if soft_surface:
        reasoning.append("hard_surface_without_rubber")
    if soft_milk:
        drop_pct = round(((milk_yield_current - milk_yield_expected) / milk_yield_expected) * 100, 1)
        reasoning.append(f"milk_yield_drop_{drop_pct}%")
    if soft_trim:
        reasoning.append(f"overgrown_hooves_{days_since_last_trim}d")
    if soft_lesions:
        reasoning.append("visible_lesions")

    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=[verdict],
        primary_rule=RULE_ID,
        action=action,
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "locomotion_score": locomotion_score,
                "bcs": bcs,
                "bedding_score": bedding_score,
                "surface_type": surface_type,
                "milk_yield_current": milk_yield_current,
                "milk_yield_expected": milk_yield_expected,
                "days_since_last_trim": days_since_last_trim,
                "visible_lesions": visible_lesions,
            },
        },
    )

    prediction = Prediction(
        direction={
            "locomotion_score": "improving_with_intervention",
            "milk_yield": "stabilizing",
        },
        range={
            "recovery_days": [7, 21],
            "treatment_cost": [500, 5000],
        },
        timeframe="14-30 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
