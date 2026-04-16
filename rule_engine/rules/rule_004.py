"""
RULE-004: Dry-Period-Nutrition-Optimization
Prevention protocol for dry period based on Litherland 2025.
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-004"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-004.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    dim = input_data.get("dim")
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    bcs_dry_off = input_data.get("bcs_dry_off") or case.get("bcs_dry_off")
    bcs_current = input_data.get("bcs_current") or case.get("bcs_current")
    previous_sck = input_data.get("previous_sck", False) or case.get("previous_sck", False)
    previous_da = input_data.get("previous_da", False) or case.get("previous_da", False)

    # ═══════════════════════════════════════════════════════
    # БЛОКИРУЮЩАЯ ВЕТКА
    # ═══════════════════════════════════════════════════════
    if clinical_signs:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_004_BLOCKED"],
            primary_rule=RULE_ID,
            action="TREAT_ILLNESS_FIRST",
            reasoning=["clinical_illness_during_dry_period"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(dim, int):
        return None, None

    # ═══════════════════════════════════════════════════════
    # HARD CONDITIONS: must be in dry period (prepartum)
    # ═══════════════════════════════════════════════════════
    if dim >= 0:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_004_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="USE_LACTATION_PROTOCOLS",
            reasoning=["not_in_dry_period"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim}},
        )
        return decision, None

    # BCS assessment required
    bcs_available = (
        isinstance(bcs_dry_off, (int, float))
        and isinstance(bcs_current, (int, float))
    )
    if not bcs_available:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_004_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="GATHER_BCS_DATA",
            reasoning=["bcs_assessment_unavailable"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # ═══════════════════════════════════════════════════════
    # SOFT CONDITIONS
    # ═══════════════════════════════════════════════════════
    soft_over_conditioned = bcs_dry_off > 3.5
    soft_bcs_gain = (bcs_current - bcs_dry_off) > 0
    soft_previous_issues = bool(previous_sck or previous_da)

    soft_score = sum([soft_over_conditioned, soft_bcs_gain, soft_previous_issues])

    if soft_score >= 2:
        verdict = "RULE_004_RECOMMENDED_HIGH"
        action = "INTENSIVE_INTERVENTION"
        confidence = "HIGH"
    elif soft_score == 1:
        verdict = "RULE_004_RECOMMENDED_MEDIUM"
        action = "ACTIVE_CORRECTION"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_004_RECOMMENDED_LOW"
        action = "STANDARD_OPTIMIZATION"
        confidence = "LOW"

    reasoning = ["in_dry_period", "bcs_assessed"]
    if soft_over_conditioned:
        reasoning.append(f"bcs_dry_off_{bcs_dry_off}_>_3.5")
    if soft_bcs_gain:
        reasoning.append(f"bcs_gain_dry_period_{round(bcs_current - bcs_dry_off, 2)}")
    if soft_previous_issues:
        reasoning.append("previous_lactation_metabolic_issues")

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
                "bcs_dry_off": bcs_dry_off,
                "bcs_current": bcs_current,
                "previous_sck": previous_sck,
                "previous_da": previous_da,
            },
        },
    )

    prediction = Prediction(
        direction={
            "bcs_at_calving": "stable_or_optimal",
            "ketosis_risk": "reduced",
        },
        range={
            "bcs_at_calving": [3.0, 3.5],
            "clinical_ketosis_rate": [0.0, 0.08],
        },
        timeframe="dry period to 30 DIM",
        confidence=confidence.lower(),
    )

    return decision, prediction
