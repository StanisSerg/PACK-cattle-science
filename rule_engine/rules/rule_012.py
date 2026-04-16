"""
RULE-012: Milk-Yield-Deviation-Alert
Productivity monitoring based on lactation curve deviation
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-012"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-012.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    is_lactating = input_data.get("is_lactating", True)
    veterinary_hold = input_data.get("veterinary_hold", False)
    dry_cow = input_data.get("dry_cow", False)

    dim = input_data.get("dim")
    parity = input_data.get("parity") if input_data.get("parity") is not None else case.get("parity")
    milk_yield_actual = input_data.get("milk_yield_actual")
    milk_yield_expected = input_data.get("milk_yield_expected")
    milk_yield_peak = input_data.get("milk_yield_peak")
    peak_week = input_data.get("peak_week")

    # BLOCKING / NOT APPLICABLE
    if dry_cow or not is_lactating:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_012_BLOCKED"],
            primary_rule=RULE_ID,
            action="USE_DRY_COW_PROTOCOL",
            reasoning=["not_lactating_or_dry_cow"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if veterinary_hold:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_012_BLOCKED"],
            primary_rule=RULE_ID,
            action="ALREADY_UNDER_TREATMENT",
            reasoning=["veterinary_hold_active"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(dim, int) or not isinstance(milk_yield_actual, (int, float)):
        return None, None

    if not isinstance(milk_yield_expected, (int, float)) or milk_yield_expected <= 0:
        return None, None

    deviation_pct = ((milk_yield_actual - milk_yield_expected) / milk_yield_expected) * 100

    # Persistence drop check
    persistence_drop = False
    if isinstance(milk_yield_peak, (int, float)) and milk_yield_peak > 0 and dim > 60:
        expected_at_dim = milk_yield_peak * (0.9985 ** (dim - 60))
        if milk_yield_actual < expected_at_dim * 0.90:
            persistence_drop = True

    # Peak timing abnormal
    peak_timing_abnormal = False
    if isinstance(peak_week, (int, float)):
        peak_timing_abnormal = peak_week < 3 or peak_week > 10

    # Determine verdict
    if deviation_pct > 20 and dim < 60:
        verdict = "RULE_012_HYPERPRODUCTIVE_RISK"
        action = "INTENSIFY_METABOLIC_MONITORING_+_ENERGY_SUPPORT"
        confidence = "HIGH"
    elif deviation_pct < -20:
        verdict = "RULE_012_CRITICAL_NEGATIVE"
        action = "IMMEDIATE_HEALTH_SCREENING_+_NUTRITION_CHECK"
        confidence = "HIGH"
    elif -20 <= deviation_pct < -10:
        verdict = "RULE_012_MODERATE_NEGATIVE"
        action = "REVIEW_WITHIN_48_HOURS"
        confidence = "MEDIUM"
    elif persistence_drop:
        verdict = "RULE_012_PERSISTENCE_ALERT"
        action = "REVIEW_MID_LACTATION_RATION_+_BODY_CONDITION"
        confidence = "MEDIUM"
    elif peak_timing_abnormal:
        verdict = "RULE_012_MODERATE_NEGATIVE"
        action = "REVIEW_PEAK_TIMING_+_NUTRITION_HEALTH"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_012_WITHIN_RANGE"
        action = "CONTINUE_ROUTINE_MONITORING"
        confidence = "LOW"

    reasoning = [f"dim_{dim}", f"milk_yield_{milk_yield_actual}_vs_expected_{milk_yield_expected}", f"deviation_{round(deviation_pct, 1)}%"]
    if persistence_drop:
        reasoning.append("persistence_drop_detected")
    if peak_timing_abnormal:
        reasoning.append(f"abnormal_peak_timing_week_{peak_week}")

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
                "milk_yield_actual": milk_yield_actual,
                "milk_yield_expected": milk_yield_expected,
                "milk_yield_peak": milk_yield_peak,
                "peak_week": peak_week,
                "deviation_pct": round(deviation_pct, 2),
            },
        },
    )

    prediction = Prediction(
        direction={
            "milk_yield_trend": "recovering_with_intervention" if deviation_pct < -10 else "stable",
            "economic_impact": "positive_if_early_intervention",
        },
        range={
            "days_to_recovery": [3, 14],
            "milk_saved_kg": [5.0, 50.0],
        },
        timeframe="7-14 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
