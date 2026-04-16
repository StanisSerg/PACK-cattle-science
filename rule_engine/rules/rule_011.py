"""
RULE-011: Mastitis-Protocol
Udder health intervention for lactating cows
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-011"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-011.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    is_lactating = input_data.get("is_lactating", True)
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    scc = input_data.get("scc")
    cmt_score = input_data.get("cmt_score")
    udder_swelling = input_data.get("udder_swelling", False)
    toxic_milk = input_data.get("toxic_milk", False)
    systemic_illness = input_data.get("systemic_illness", False)
    cases_this_lactation = input_data.get("cases_this_lactation", 0)
    same_quarter_cases = input_data.get("same_quarter_cases", 0)
    dim = input_data.get("dim")
    culture_result = input_data.get("culture_result")
    pathogen = input_data.get("pathogen")

    # BLOCKING: Gangrenous or septic mastitis
    severe_signs = {"udder_gangrene", "systemic_toxicosis", "recumbency"}
    if severe_signs.intersection(set(clinical_signs)) or toxic_milk:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_011_BLOCKED"],
            primary_rule=RULE_ID,
            action="REFER_TO_EMERGENCY_VETERINARY_PROTOCOL",
            reasoning=["gangrenous_or_severe_systemic_mastitis"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not is_lactating:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_011_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="USE_DRY_COW_MASTITIS_PROTOCOL",
            reasoning=["not_lactating"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # HARD: mastitis suspected or confirmed
    hard_trigger = (
        bool(clinical_signs)
        or (isinstance(scc, (int, float)) and scc > 400000)
        or (isinstance(cmt_score, (int, float)) and cmt_score >= 3)
        or bool(udder_swelling)
    )

    if not hard_trigger:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_011_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="CONTINUE_UDDER_HEALTH_MONITORING",
            reasoning=["no_mastitis_indicators"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    # Determine severity and history
    severe_clinical = bool(clinical_signs) and (bool(udder_swelling) or bool(toxic_milk))
    repeated_chronic = (
        (isinstance(cases_this_lactation, (int, float)) and cases_this_lactation >= 3)
        or (isinstance(same_quarter_cases, (int, float)) and same_quarter_cases >= 2)
        or (isinstance(scc, (int, float)) and scc > 400000)
    )
    culture_available = bool(culture_result) or bool(pathogen)
    late_lactation = isinstance(dim, int) and dim > 250

    if severe_clinical and systemic_illness:
        verdict = "RULE_011_EMERGENCY"
        action = "SYSTEMIC_ANTIBIOTIC_+_ANTIINFLAMMATORY_+_UDDER_SUPPORT"
        confidence = "HIGH"
    elif repeated_chronic and (isinstance(cases_this_lactation, (int, float)) and cases_this_lactation >= 3):
        verdict = "RULE_011_CHRONIC_CULL_CANDIDATE"
        action = "CULTURE_MANDATORY_+_ECONOMIC_REVIEW"
        confidence = "HIGH"
    elif culture_available:
        verdict = "RULE_011_TARGETED_TREATMENT"
        action = "INTRAMAMMARY_THERAPY_PER_CULTURE"
        confidence = "MEDIUM"
    elif bool(clinical_signs) and not culture_available:
        verdict = "RULE_011_BLIND_TREATMENT"
        action = "STANDARD_INTRAMAMMARY_+_TAKE_CULTURE_BEFORE_FIRST_TREATMENT"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_011_MONITOR_CULTURE"
        action = "CULTURE_FIRST_+_TREAT_IF_GRAM_POSITIVE"
        confidence = "LOW"

    reasoning = []
    if clinical_signs:
        reasoning.append("clinical_signs_present")
    if isinstance(scc, (int, float)) and scc > 400000:
        reasoning.append(f"scc_{scc}_>_400k")
    if isinstance(cmt_score, (int, float)) and cmt_score >= 3:
        reasoning.append(f"cmt_score_{cmt_score}")
    if udder_swelling:
        reasoning.append("udder_swelling")

    if severe_clinical:
        reasoning.append("severe_clinical_mastitis")
    if isinstance(cases_this_lactation, (int, float)) and cases_this_lactation >= 3:
        reasoning.append(f"cases_this_lactation_{cases_this_lactation}")
    if isinstance(same_quarter_cases, (int, float)) and same_quarter_cases >= 2:
        reasoning.append(f"same_quarter_cases_{same_quarter_cases}")
    if culture_available:
        reasoning.append("culture_available")
    if late_lactation:
        reasoning.append(f"late_lactation_dim_{dim}")

    decision = Decision(
        triggered_rules=[RULE_ID],
        verdicts=[verdict],
        primary_rule=RULE_ID,
        action=action,
        reasoning=reasoning,
        basis={
            "rule": RULE_ID,
            "conditions": {
                "scc": scc,
                "cmt_score": cmt_score,
                "clinical_signs": clinical_signs,
                "udder_swelling": udder_swelling,
                "cases_this_lactation": cases_this_lactation,
                "same_quarter_cases": same_quarter_cases,
                "culture_result": culture_result,
                "pathogen": pathogen,
                "dim": dim,
            },
        },
    )

    prediction = Prediction(
        direction={
            "clinical_cure": "expected_with_appropriate_therapy",
            "scc": "trending_down_if_cured",
        },
        range={
            "milk_return_to_tank_day": [5, 10],
            "scc_day_14": [50000, 200000],
        },
        timeframe="7-14 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
