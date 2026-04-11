"""
RULE-002: SCK-BHB-Threshold
SCK screening rule
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-002"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-002
    
    Returns:
        (Decision, Prediction) или (None, None) если условия не met
    """
    input_data = case.get("input", {})
    derived = case.get("derived", {})

    bhb = input_data.get("bhb")
    dim = input_data.get("dim")
    clinical_signs = input_data.get("clinical_signs", [])

    if not isinstance(clinical_signs, list):
        clinical_signs = []

    # BLOCKING: Clinical signs present
    if clinical_signs:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_002_BLOCKED"],
            primary_rule=RULE_ID,
            action="USE_CLINICAL_PROTOCOL",
            reasoning=["clinical_signs_present"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(bhb, (int, float)) or not isinstance(dim, int):
        return None, None

    # GRAY ZONE: BHB 1.0-1.2
    if 1.0 <= bhb < 1.2 and 3 <= dim <= 14:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_002_GRAY_ZONE"],
            primary_rule=RULE_ID,
            action="MONITOR_AND_REPEAT_BHB_3_5_DAYS",
            reasoning=["bhb_gray_zone_1.0_1.2", "early_postpartum_dim_3_14"],
            basis={
                "rule": RULE_ID,
                "conditions": {"bhb": bhb, "dim": dim}
            },
        )
        prediction = Prediction(
            direction={"bhb": "uncertain"},
            range={"bhb_day_3_7": [1.0, 1.4]},
            timeframe="3-7 days",
            confidence="low",
        )
        return decision, prediction

    # TRIGGERED: BHB >= 1.2
    if bhb >= 1.2 and 3 <= dim <= 14:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_002_TRIGGERED"],
            primary_rule=RULE_ID,
            action="ESCALATE_TO_RULE_001_AND_RULE_003_CHECK",
            reasoning=[
                f"bhb_{bhb}>=1.2",
                f"dim_{dim}_in_3_14",
                "no_clinical_signs"
            ],
            basis={
                "rule": RULE_ID,
                "conditions": {
                    "bhb": bhb,
                    "dim": dim,
                    "dmi_ratio": derived.get("dmi_ratio"),
                },
            },
        )
        prediction = Prediction(
            direction={"bhb": "may_increase_without_intervention"},
            range={"bhb_day_3_7_no_treatment": [1.2, 2.0]},
            timeframe="3-7 days",
            confidence="medium",
        )
        return decision, prediction

    # NOT TRIGGERED
    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=["RULE_002_NOT_TRIGGERED"],
        primary_rule=RULE_ID,
        action="CONTINUE_MONITORING",
        reasoning=["screening_threshold_not_met"],
        basis={"rule": RULE_ID, "conditions": {"bhb": bhb, "dim": dim}},
    )
    return decision, None
