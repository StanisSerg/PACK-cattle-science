"""
RULE-008: Heat-Stress-Intervention
Environmental management for dairy cattle when THI > 68
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-008"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-008.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    thi = input_data.get("thi")
    if thi is None:
        temperature_c = input_data.get("temperature_c")
        humidity_pct = input_data.get("humidity_pct")
        if isinstance(temperature_c, (int, float)) and isinstance(humidity_pct, (int, float)):
            # THI = T - (0.55 - 0.0055 * RH) * (T - 14.5)
            thi = temperature_c - (0.55 - 0.0055 * humidity_pct) * (temperature_c - 14.5)

    dmi_ratio = input_data.get("dmi_ratio")
    if dmi_ratio is None:
        dmi_actual = input_data.get("dmi_actual")
        dmi_baseline = input_data.get("dmi_baseline")
        if isinstance(dmi_actual, (int, float)) and isinstance(dmi_baseline, (int, float)) and dmi_baseline > 0:
            dmi_ratio = dmi_actual / dmi_baseline

    milk_yield_current = input_data.get("milk_yield_current")
    milk_yield_baseline = input_data.get("milk_yield_baseline")
    peak_yield = input_data.get("peak_yield", 0)
    cooling_fans = input_data.get("cooling_fans_available", True)
    cooling_soak = input_data.get("cooling_soak_available", True)
    full_cooling_active = input_data.get("full_cooling_active", False)

    if not isinstance(thi, (int, float)):
        return None, None

    # BLOCKING: full cooling already active but THI still rising
    if full_cooling_active and thi > 72:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_008_BLOCKED"],
            primary_rule=RULE_ID,
            action="ESCALATE_TO_ENGINEERING_REVIEW",
            reasoning=["full_cooling_active_but_thi_still_high"],
            basis={"rule": RULE_ID, "conditions": {"thi": thi}},
        )
        return decision, None

    if thi <= 68:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_008_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="NO_HEAT_STRESS_INTERVENTION_NEEDED",
            reasoning=["thi_within_normal_range"],
            basis={"rule": RULE_ID, "conditions": {"thi": round(thi, 1)}},
        )
        return decision, None

    # SOFT conditions
    soft_severe = thi > 72
    soft_dmi = isinstance(dmi_ratio, (int, float)) and dmi_ratio < 0.9
    soft_milk = (
        isinstance(milk_yield_current, (int, float))
        and isinstance(milk_yield_baseline, (int, float))
        and milk_yield_baseline > 0
        and (milk_yield_current - milk_yield_baseline) / milk_yield_baseline < -0.10
    )
    soft_high_producer = isinstance(peak_yield, (int, float)) and peak_yield > 35
    soft_infrastructure = not bool(cooling_fans) or not bool(cooling_soak)

    soft_score = sum([soft_severe, soft_dmi, soft_milk, soft_high_producer, soft_infrastructure])

    if soft_score >= 3:
        verdict = "RULE_008_HIGH_RISK"
        action = "FULL_COOLING_PROTOCOL_+_RATION_ADJUSTMENTS"
        confidence = "HIGH"
    elif soft_score >= 1:
        verdict = "RULE_008_MEDIUM_RISK"
        action = "ENHANCED_COOLING_+_MONITOR_DMI"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_008_LOW_RISK"
        action = "PREVENTIVE_COOLING_ACTIVATION"
        confidence = "LOW"

    reasoning = [f"thi_{round(thi, 1)}_>_68"]
    if soft_severe:
        reasoning.append("severe_heat_stress_thi>72")
    if soft_dmi:
        reasoning.append(f"dmi_ratio_{round(dmi_ratio, 2)}_<_0.9")
    if soft_milk:
        drop_pct = round(((milk_yield_current - milk_yield_baseline) / milk_yield_baseline) * 100, 1)
        reasoning.append(f"milk_yield_drop_{drop_pct}%")
    if soft_high_producer:
        reasoning.append(f"high_producer_{peak_yield}L")
    if soft_infrastructure:
        reasoning.append("inadequate_cooling_infrastructure")

    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=[verdict],
        primary_rule=RULE_ID,
        action=action,
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "thi": round(thi, 1),
                "dmi_ratio": dmi_ratio,
                "milk_yield_current": milk_yield_current,
                "milk_yield_baseline": milk_yield_baseline,
                "peak_yield": peak_yield,
                "cooling_fans_available": cooling_fans,
                "cooling_soak_available": cooling_soak,
            },
        },
    )

    prediction = Prediction(
        direction={
            "milk_yield": "stabilize_with_intervention",
            "dmi": "recover_with_cooling",
        },
        range={
            "milk_loss_prevented_L_per_day": [1.0, 4.0],
        },
        timeframe="0-7 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
