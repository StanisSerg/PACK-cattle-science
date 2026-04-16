"""
RULE-005: Hypocalcemia-Milk-Fever-Prevention-and-Treatment
DCAD prevention and emergency calcium treatment.
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-005"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-005.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    dim = input_data.get("dim")
    parity = input_data.get("parity") if input_data.get("parity") is not None else case.get("parity")
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    breed = input_data.get("breed", "Holstein") or case.get("breed", "Holstein")
    previous_milk_fever = input_data.get("previous_milk_fever", False) or case.get("previous_milk_fever", False)
    bcs_dry_off = input_data.get("bcs_dry_off") if input_data.get("bcs_dry_off") is not None else case.get("bcs_dry_off")
    total_ca = input_data.get("total_ca") if input_data.get("total_ca") is not None else case.get("total_ca")
    ionized_ca = input_data.get("ionized_ca") if input_data.get("ionized_ca") is not None else case.get("ionized_ca")

    if not isinstance(parity, int) or not isinstance(dim, int):
        return None, None

    # ═══════════════════════════════════════════════════════
    # EMERGENCY MODE (postpartum)
    # ═══════════════════════════════════════════════════════
    if dim >= 0:
        milk_fever_signs = {"sternal_recumbency", "weakness", "cold_ears", "bloat"}
        if milk_fever_signs.intersection(set(clinical_signs)):
            decision = Decision(
                triggered_rules=[RULE_ID],
                verdicts=["RULE_005_EMERGENCY_IV_CALCIUM"],
                primary_rule=RULE_ID,
                action="IV_CALCIUM_BOROGLUCONATE_500_800ML",
                reasoning=["clinical_milk_fever_signs"],
                basis={"rule": RULE_ID, "conditions": {"clinical_signs": clinical_signs}},
            )
            return decision, None

        subclinical = False
        if isinstance(total_ca, (int, float)) and total_ca < 2.0:
            subclinical = True
        if isinstance(ionized_ca, (int, float)) and ionized_ca < 1.0:
            subclinical = True

        if subclinical:
            decision = Decision(
                triggered_rules=[RULE_ID],
                verdicts=["RULE_005_ORAL_CALCIUM_PROTOCOL"],
                primary_rule=RULE_ID,
                action="ORAL_CALCIUM_SUPPLEMENTATION",
                reasoning=["subclinical_hypocalcemia_confirmed"],
                basis={
                    "rule": RULE_ID,
                    "conditions": {"total_ca": total_ca, "ionized_ca": ionized_ca},
                },
            )
            return decision, None

        high_risk_at_calving = (
            str(breed).lower() == "jersey"
            or bool(previous_milk_fever)
            or parity >= 3
        )
        if high_risk_at_calving:
            decision = Decision(
                triggered_rules=[RULE_ID],
                verdicts=["RULE_005_PROPHYLACTIC_CALCIUM"],
                primary_rule=RULE_ID,
                action="PROPHYLACTIC_CALCIUM_AT_CALVING",
                reasoning=["high_risk_at_calving"],
                basis={
                    "rule": RULE_ID,
                    "conditions": {
                        "breed": breed,
                        "parity": parity,
                        "previous_milk_fever": previous_milk_fever,
                    },
                },
            )
            prediction = Prediction(
                direction={"milk_fever_risk": "reduced"},
                range={"clinical_hypocalcemia": [0.0, 0.05]},
                timeframe="0-48 hours",
                confidence="medium",
            )
            return decision, prediction

        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_005_MONITOR_PREVENTIVELY"],
            primary_rule=RULE_ID,
            action="CONTINUE_MONITORING",
            reasoning=["no_emergency_indicators"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim, "parity": parity}},
        )
        return decision, None

    # ═══════════════════════════════════════════════════════
    # PREVENTION MODE (prepartum)
    # ═══════════════════════════════════════════════════════
    if parity == 1:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_005_BLOCKED"],
            primary_rule=RULE_ID,
            action="USE_POSITIVE_DCAD_OR_STANDARD_DIET",
            reasoning=["first_lactation_heifer_excluded"],
            basis={"rule": RULE_ID, "conditions": {"parity": parity}},
        )
        return decision, None

    if dim > -21:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_005_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="MONITOR_UNTIL_CLOSE_UP",
            reasoning=["too_early_for_dcadc_prevention"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim}},
        )
        return decision, None

    # SOFT conditions
    soft_breed = (
        str(breed).lower() == "jersey"
        or input_data.get("high_producing_holstein", False)
    )
    soft_previous = bool(previous_milk_fever)
    soft_bcs = isinstance(bcs_dry_off, (int, float)) and bcs_dry_off > 3.5
    soft_age = parity >= 3

    soft_score = sum([soft_breed, soft_previous, soft_bcs, soft_age])

    if soft_score >= 2:
        verdict = "RULE_005_DCAD_RECOMMENDED_HIGH"
        dcad_target = "-150"
        confidence = "HIGH"
    elif soft_score == 1:
        verdict = "RULE_005_DCAD_RECOMMENDED_MEDIUM"
        dcad_target = "-100_to_-120"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_005_DCAD_RECOMMENDED_LOW"
        dcad_target = "-50"
        confidence = "LOW"

    reasoning = ["multiparous", "within_21_days_of_calving"]
    if soft_breed:
        reasoning.append("high_risk_breed")
    if soft_previous:
        reasoning.append("previous_milk_fever")
    if soft_bcs:
        reasoning.append(f"bcs_dry_off_{bcs_dry_off}_>_3.5")
    if soft_age:
        reasoning.append("parity_>=_3")

    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=[verdict],
        primary_rule=RULE_ID,
        action="IMPLEMENT_NEGATIVE_DCAD",
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "dim": dim,
                "parity": parity,
                "breed": breed,
                "previous_milk_fever": previous_milk_fever,
                "bcs_dry_off": bcs_dry_off,
                "dcad_target": dcad_target,
            },
        },
    )

    prediction = Prediction(
        direction={
            "urine_ph": "target_6.0_6.5",
            "milk_fever_risk": "reduced",
        },
        range={
            "urine_ph": [6.0, 6.5],
            "clinical_milk_fever_rate": [0.0, 0.02],
        },
        timeframe="close-up period",
        confidence=confidence.lower(),
    )

    return decision, prediction
