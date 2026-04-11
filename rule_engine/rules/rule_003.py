"""
RULE-003: Propylene-Glycol-Protocol
PG treatment rule
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-003"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-003
    
    Returns:
        (Decision, Prediction) или (None, None) если условия не met
    """
    input_data = case.get("input", {})
    clinical_signs = input_data.get("clinical_signs", [])

    if not isinstance(clinical_signs, list):
        clinical_signs = []

    bhb = input_data.get("bhb")
    dim = input_data.get("dim")
    can_swallow = input_data.get("can_swallow", True)
    severe_hepatic_lipidosis = input_data.get("severe_hepatic_lipidosis", False)
    anorexia_hours = input_data.get("anorexia_hours", 0)

    if not isinstance(bhb, (int, float)) or not isinstance(dim, int):
        return None, None

    # BLOCKED: Clinical signs present
    if clinical_signs:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_003_BLOCKED"],
            primary_rule=RULE_ID,
            action="USE_CLINICAL_KETOSIS_EMERGENCY_PROTOCOL",
            reasoning=["clinical_signs_present"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # NOT APPLICABLE: Severe SCK
    if bhb > 2.9:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_003_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="ESCALATE_TO_COMBINED_THERAPY",
            reasoning=["severe_sck_bhb>2.9"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # BLOCKED: Cannot administer oral PG
    if not can_swallow or anorexia_hours > 48 or severe_hepatic_lipidosis:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_003_BLOCKED"],
            primary_rule=RULE_ID,
            action="ESCALATE_TO_PARENTERAL_OR_SPECIALIZED_CARE",
            reasoning=["oral_pg_not_applicable"],
            basis={
                "rule": RULE_ID,
                "conditions": {
                    "can_swallow": can_swallow,
                    "anorexia_hours": anorexia_hours,
                    "severe_hepatic_lipidosis": severe_hepatic_lipidosis,
                },
            },
        )
        return decision, None

    # APPLICABLE: SCK confirmed, PG can be used
    if 1.2 <= bhb <= 2.9 and 3 <= dim <= 14:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_003_APPLICABLE"],
            primary_rule=RULE_ID,
            action="PG_300ML_X_5_DAYS_2X_DAILY",
            reasoning=["sck_confirmed", "bhb_in_range", "oral_pg_applicable"],
            basis={
                "rule": RULE_ID,
                "conditions": {"bhb": bhb, "dim": dim}
            },
        )
        prediction = Prediction(
            direction={
                "bhb": "down",
                "dmi": "up",
            },
            range={
                "bhb_day_7": [0.6, 0.9],
                "dmi_day_7": [14.0, 18.0],
            },
            timeframe="7 days",
            confidence="medium",
        )
        return decision, prediction

    # NOT TRIGGERED
    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=["RULE_003_NOT_TRIGGERED"],
        primary_rule=RULE_ID,
        action="NO_PG_PROTOCOL",
        reasoning=["treatment_threshold_not_met"],
        basis={"rule": RULE_ID, "conditions": {"bhb": bhb, "dim": dim}},
    )
    return decision, None
