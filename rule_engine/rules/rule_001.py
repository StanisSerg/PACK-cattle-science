"""
RULE-001: Ketosis-Threshold-Invalidation
IF BHB > 1.2 AND DIM < 30 THEN do not apply hepatoprotectors as primary solution;
correct system instead.
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-001"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-001.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})
    derived = case.get("derived", {})

    bhb = input_data.get("bhb")
    dim = input_data.get("dim")
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    # ═══════════════════════════════════════════════════════
    # БЛОК 1: БЛОКИРУЮЩАЯ ВЕТКА
    # ═══════════════════════════════════════════════════════
    if clinical_signs:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_001_BLOCKED"],
            primary_rule=RULE_ID,
            action="REFER_TO_CLINICAL_PROTOCOL",
            reasoning=["clinical_signs_present: " + ", ".join(clinical_signs)],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(bhb, (int, float)) or not isinstance(dim, int):
        return None, None

    # ═══════════════════════════════════════════════════════
    # БЛОК 2: HARD CONDITIONS
    # ═══════════════════════════════════════════════════════
    hard_bhb = bhb > 1.2
    hard_dim = dim < 30
    hard_met = hard_bhb and hard_dim

    if not hard_met:
        reasons = []
        if not hard_bhb:
            reasons.append(f"bhb_{bhb}_<=_1.2")
        if not hard_dim:
            reasons.append(f"dim_{dim}_>=_30")
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_001_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="GATHER_MORE_DATA",
            reasoning=reasons,
            basis={"rule": RULE_ID, "conditions": {"bhb": bhb, "dim": dim}},
        )
        return decision, None

    # ═══════════════════════════════════════════════════════
    # БЛОК 3: SOFT CONDITIONS
    # ═══════════════════════════════════════════════════════
    dmi_ratio = derived.get("dmi_ratio")
    bcs_loss = derived.get("bcs_loss")

    soft_dmi = False
    soft_bcs = False
    if isinstance(dmi_ratio, (int, float)):
        soft_dmi = dmi_ratio < 0.8
    if isinstance(bcs_loss, (int, float)):
        soft_bcs = bcs_loss > 0.5

    soft_score = sum([soft_dmi, soft_bcs])

    # ═══════════════════════════════════════════════════════
    # БЛОК 4: CONFIDENCE
    # ═══════════════════════════════════════════════════════
    if soft_score == 2:
        confidence = "HIGH"
    elif soft_score == 1:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    # ═══════════════════════════════════════════════════════
    # БЛОК 5: REASONING
    # ═══════════════════════════════════════════════════════
    reasoning = [
        f"bhb_{bhb}_>_1.2_hard",
        f"dim_{dim}_<_30_hard",
    ]
    if soft_dmi:
        reasoning.append(f"dmi_ratio_{dmi_ratio}_<_0.8_soft")
    if soft_bcs:
        reasoning.append(f"bcs_loss_{bcs_loss}_>_0.5_soft")

    # ═══════════════════════════════════════════════════════
    # БЛОК 6: ФИНАЛЬНЫЙ ВЕРДИКТ
    # ═══════════════════════════════════════════════════════
    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=["RULE_001_TRIGGERED"],
        primary_rule=RULE_ID,
        action="DO_NOT_USE_AS_PRIMARY_INTERVENTION",
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "bhb": bhb,
                "dim": dim,
                "dmi_ratio": dmi_ratio,
                "bcs_loss": bcs_loss,
            },
        },
    )

    prediction = Prediction(
        direction={
            "bhb": "down_with_systemic_correction",
            "dmi": "up",
        },
        range={
            "bhb_day_7": [0.4, 0.9],
            "dmi_day_7": [14.0, 19.0],
        },
        timeframe="7 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
