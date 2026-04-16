"""
RULE-007: Displaced-Abomasum-Risk-Screening
Early DA risk detection based on ketosis, DMI depression, and pH changes
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-007"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-007.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})
    derived = case.get("derived", {})

    dim = input_data.get("dim")
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    bhb = input_data.get("bhb")
    dmi_ratio = derived.get("dmi_ratio")
    if dmi_ratio is None:
        dmi_actual = input_data.get("dmi_actual")
        dmi_norm = input_data.get("dmi_norm")
        if isinstance(dmi_actual, (int, float)) and isinstance(dmi_norm, (int, float)) and dmi_norm > 0:
            dmi_ratio = dmi_actual / dmi_norm

    ruminal_ph = input_data.get("ruminal_ph")
    previous_da = input_data.get("previous_da", False)
    peak_yield = input_data.get("peak_yield", 0)

    # BLOCKING: Clinical DA already confirmed
    da_signs = {"pinging_left", "abomasal_tympany", "scissor_posture", "complete_anorexia"}
    if da_signs.intersection(set(clinical_signs)):
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_007_BLOCKED"],
            primary_rule=RULE_ID,
            action="REFER_TO_SURGICAL_PROTOCOL_IMMEDIATELY",
            reasoning=["clinical_da_confirmed"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(dim, int):
        return None, None

    # HARD: window 5-30 DIM
    if not (5 <= dim <= 30):
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_007_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="USE_STANDARD_POSTPARTUM_MONITORING",
            reasoning=["outside_da_risk_window_5_30_dim"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim}},
        )
        return decision, None

    # HARD: at least one primary risk factor
    primary_risk = False
    if isinstance(bhb, (int, float)) and bhb >= 1.2:
        primary_risk = True
    if isinstance(dmi_ratio, (int, float)) and dmi_ratio < 0.7:
        primary_risk = True
    if isinstance(ruminal_ph, (int, float)) and ruminal_ph > 7.0:
        primary_risk = True

    if not primary_risk:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_007_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="CONTINUE_STANDARD_MONITORING",
            reasoning=["no_primary_da_risk_factors"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim, "bhb": bhb, "dmi_ratio": dmi_ratio, "ruminal_ph": ruminal_ph}},
        )
        return decision, None

    # SOFT conditions
    soft_ketosis = isinstance(bhb, (int, float)) and bhb >= 1.4
    soft_dmi = isinstance(dmi_ratio, (int, float)) and dmi_ratio < 0.6
    soft_high_producer = isinstance(peak_yield, (int, float)) and peak_yield > 40
    soft_previous_da = bool(previous_da)

    soft_score = sum([soft_ketosis, soft_dmi, soft_high_producer, soft_previous_da])

    if soft_score >= 3:
        verdict = "RULE_007_HIGH_RISK"
        action = "ACTIVE_INTERVENTION_+_VET_ON_STANDBY"
        confidence = "HIGH"
    elif soft_score >= 1:
        verdict = "RULE_007_MEDIUM_RISK"
        action = "ENHANCED_MONITORING_+_RUMEN_SUPPORT"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_007_LOW_RISK"
        action = "STANDARD_MONITORING"
        confidence = "LOW"

    reasoning = [f"dim_{dim}_in_da_window"]
    if isinstance(bhb, (int, float)) and bhb >= 1.2:
        reasoning.append(f"bhb_{bhb}_>=_1.2")
    if isinstance(dmi_ratio, (int, float)) and dmi_ratio < 0.7:
        reasoning.append(f"dmi_ratio_{round(dmi_ratio, 2)}_<_0.7")
    if isinstance(ruminal_ph, (int, float)) and ruminal_ph > 7.0:
        reasoning.append(f"ruminal_ph_{ruminal_ph}_>_7.0")

    if soft_ketosis:
        reasoning.append("concurrent_ketosis_bhb>=1.4")
    if soft_dmi:
        reasoning.append("severe_dmi_depression")
    if soft_high_producer:
        reasoning.append(f"high_producer_{peak_yield}L")
    if soft_previous_da:
        reasoning.append("previous_da")

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
                "bhb": bhb,
                "dmi_ratio": dmi_ratio,
                "ruminal_ph": ruminal_ph,
                "previous_da": previous_da,
                "peak_yield": peak_yield,
            },
        },
    )

    prediction = Prediction(
        direction={
            "da_risk": "elevated" if soft_score >= 2 else "present",
            "rumen_motility": "needs_support",
        },
        range={
            "clinical_da_probability": [0.05, 0.25] if soft_score >= 3 else [0.02, 0.12],
        },
        timeframe="5-14 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
