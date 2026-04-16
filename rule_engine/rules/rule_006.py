"""
RULE-006: Metritis-Retained-Placenta-Protocol
Postpartum reproductive intervention
"""
from __future__ import annotations

from typing import Any

from models import Decision, Prediction


RULE_ID = "RULE-006"


def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    """
    Оценить кейс по RULE-006.

    Returns:
        (Decision, Prediction) или (None, None) если недостаточно данных.
    """
    input_data = case.get("input", {})

    dim = input_data.get("dim")
    parity = input_data.get("parity") if input_data.get("parity") is not None else case.get("parity")
    clinical_signs = input_data.get("clinical_signs", [])
    if not isinstance(clinical_signs, list):
        clinical_signs = []

    retained_placenta_hours = input_data.get("retained_placenta_hours", 0)
    fever = input_data.get("fever")
    foul_smelling_discharge = input_data.get("foul_smelling_discharge", False)
    uterine_tenderness = input_data.get("uterine_tenderness", False)
    dystocia = input_data.get("dystocia", False)
    twinning = input_data.get("twinning", False)
    bhb = input_data.get("bhb")
    total_ca = input_data.get("total_ca")

    severe_systemic_illness = input_data.get("severe_systemic_illness", False)
    septic_shock = input_data.get("septic_shock", False)

    # ═══════════════════════════════════════════════════════
    # БЛОКИРУЮЩАЯ ВЕТКА
    # ═══════════════════════════════════════════════════════
    if severe_systemic_illness or septic_shock:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_006_BLOCKED"],
            primary_rule=RULE_ID,
            action="REFER_TO_EMERGENCY_VETERINARY_PROTOCOL",
            reasoning=["severe_systemic_illness_or_septic_shock"],
            basis={"rule": RULE_ID},
        )
        return decision, None

    if not isinstance(dim, int):
        return None, None

    # ═══════════════════════════════════════════════════════
    # HARD CONDITIONS: must be in early postpartum window
    # ═══════════════════════════════════════════════════════
    if not (1 <= dim <= 21):
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_006_NOT_APPLICABLE"],
            primary_rule=RULE_ID,
            action="USE_REPRODUCTIVE_SPECIALIST_OR_LACTATION_PROTOCOL",
            reasoning=["outside_early_postpartum_window_1_21_dim"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim}},
        )
        return decision, None

    # Hard trigger: any uterine pathology indicator
    hard_trigger = (
        (isinstance(retained_placenta_hours, (int, float)) and retained_placenta_hours > 24)
        or (isinstance(fever, (int, float)) and fever > 39.5)
        or bool(foul_smelling_discharge)
        or bool(uterine_tenderness)
    )

    if not hard_trigger:
        decision = Decision(
            triggered_rules=[RULE_ID],
            verdicts=["RULE_006_NOT_TRIGGERED"],
            primary_rule=RULE_ID,
            action="CONTINUE_POSTPARTUM_MONITORING",
            reasoning=["no_hard_metritis_or_rp_indicators"],
            basis={"rule": RULE_ID, "conditions": {"dim": dim}},
        )
        return decision, None

    # ═══════════════════════════════════════════════════════
    # SOFT CONDITIONS
    # ═══════════════════════════════════════════════════════
    soft_metabolic = False
    if isinstance(bhb, (int, float)) and bhb > 1.2:
        soft_metabolic = True
    if isinstance(total_ca, (int, float)) and total_ca < 2.0:
        soft_metabolic = True

    soft_dystocia = bool(dystocia or twinning)
    soft_parity = isinstance(parity, int) and parity >= 3

    soft_score = sum([soft_metabolic, soft_dystocia, soft_parity])

    if soft_score >= 2:
        verdict = "RULE_006_TRIGGERED_HIGH"
        action = "SYSTEMIC_ANTIBIOTIC_+_UTERINE_THERAPY_+_METABOLIC_SUPPORT"
        confidence = "HIGH"
    elif soft_score == 1:
        verdict = "RULE_006_TRIGGERED_MEDIUM"
        action = "SYSTEMIC_ANTIBIOTIC_+_MONITORING"
        confidence = "MEDIUM"
    else:
        verdict = "RULE_006_TRIGGERED_LOW"
        action = "LOCAL_THERAPY_+_MONITORING"
        confidence = "LOW"

    reasoning = [
        f"dim_{dim}_in_early_postpartum",
        "hard_trigger_met",
    ]
    if isinstance(retained_placenta_hours, (int, float)) and retained_placenta_hours > 24:
        reasoning.append(f"retained_placenta_{retained_placenta_hours}h")
    if isinstance(fever, (int, float)) and fever > 39.5:
        reasoning.append(f"fever_{fever}")
    if foul_smelling_discharge:
        reasoning.append("foul_smelling_discharge")
    if uterine_tenderness:
        reasoning.append("uterine_tenderness")

    if soft_metabolic:
        reasoning.append("concurrent_metabolic_disorder")
    if soft_dystocia:
        reasoning.append("difficult_calving_or_twinning")
    if soft_parity:
        reasoning.append(f"parity_{parity}_>=_3")

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
                "retained_placenta_hours": retained_placenta_hours,
                "fever": fever,
                "foul_smelling_discharge": foul_smelling_discharge,
                "uterine_tenderness": uterine_tenderness,
                "bhb": bhb,
                "total_ca": total_ca,
                "dystocia": dystocia,
                "twinning": twinning,
                "parity": parity,
            },
        },
    )

    prediction = Prediction(
        direction={
            "uterine_involution": "improving",
            "milk_yield": "recovering",
        },
        range={
            "recovery_days": [3, 7],
            "conception_delay_risk": [0.0, 0.15],
        },
        timeframe="7-14 days",
        confidence=confidence.lower(),
    )

    return decision, prediction
