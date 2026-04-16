#!/usr/bin/env python3
"""
Комплексный тест всех 10 правил Rule Engine
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from models import attach_derived, load_yaml
from rules import rule_001, rule_002, rule_003, rule_004, rule_005, rule_006, rule_007, rule_008, rule_009, rule_010, rule_011, rule_012

TEST_CASES = [
    # RULE-001
    ("cases/test_suite/R001-triggered.yaml", "RULE-001", "RULE_001_TRIGGERED"),
    ("cases/test_suite/R001-blocked.yaml", "RULE-001", "RULE_001_BLOCKED"),
    ("cases/test_suite/R001-not-triggered.yaml", "RULE-001", "RULE_001_NOT_TRIGGERED"),
    # RULE-002
    ("cases/test_suite/R002-triggered.yaml", "RULE-002", "RULE_002_TRIGGERED"),
    ("cases/test_suite/R002-gray.yaml", "RULE-002", "RULE_002_GRAY_ZONE"),
    ("cases/test_suite/R002-blocked.yaml", "RULE-002", "RULE_002_BLOCKED"),
    # RULE-003
    ("cases/test_suite/R003-applicable.yaml", "RULE-003", "RULE_003_APPLICABLE"),
    ("cases/test_suite/R003-blocked.yaml", "RULE-003", "RULE_003_BLOCKED"),
    ("cases/test_suite/R003-not-applicable.yaml", "RULE-003", "RULE_003_NOT_APPLICABLE"),
    # RULE-004
    ("cases/test_suite/R004-high.yaml", "RULE-004", "RULE_004_RECOMMENDED_HIGH"),
    ("cases/test_suite/R004-medium.yaml", "RULE-004", "RULE_004_RECOMMENDED_MEDIUM"),
    ("cases/test_suite/R004-blocked.yaml", "RULE-004", "RULE_004_BLOCKED"),
    # RULE-005
    ("cases/test_suite/R005-emergency.yaml", "RULE-005", "RULE_005_EMERGENCY_IV_CALCIUM"),
    ("cases/test_suite/R005-oral.yaml", "RULE-005", "RULE_005_ORAL_CALCIUM_PROTOCOL"),
    ("cases/test_suite/R005-dcad-high.yaml", "RULE-005", "RULE_005_DCAD_RECOMMENDED_HIGH"),
    ("cases/test_suite/R005-blocked.yaml", "RULE-005", "RULE_005_BLOCKED"),
    # RULE-006
    ("cases/test_suite/R006-high.yaml", "RULE-006", "RULE_006_TRIGGERED_HIGH"),
    ("cases/test_suite/R006-medium.yaml", "RULE-006", "RULE_006_TRIGGERED_MEDIUM"),
    ("cases/test_suite/R006-low.yaml", "RULE-006", "RULE_006_TRIGGERED_LOW"),
    ("cases/test_suite/R006-blocked.yaml", "RULE-006", "RULE_006_BLOCKED"),
    ("cases/test_suite/R006-not-applicable.yaml", "RULE-006", "RULE_006_NOT_APPLICABLE"),
    # RULE-007
    ("cases/test_suite/R007-high.yaml", "RULE-007", "RULE_007_HIGH_RISK"),
    ("cases/test_suite/R007-medium.yaml", "RULE-007", "RULE_007_MEDIUM_RISK"),
    ("cases/test_suite/R007-blocked.yaml", "RULE-007", "RULE_007_BLOCKED"),
    # RULE-008
    ("cases/test_suite/R008-high.yaml", "RULE-008", "RULE_008_HIGH_RISK"),
    ("cases/test_suite/R008-low.yaml", "RULE-008", "RULE_008_LOW_RISK"),
    ("cases/test_suite/R008-not-app.yaml", "RULE-008", "RULE_008_NOT_APPLICABLE"),
    # RULE-009
    ("cases/test_suite/R009-high.yaml", "RULE-009", "RULE_009_HIGH_RISK"),
    ("cases/test_suite/R009-medium.yaml", "RULE-009", "RULE_009_MEDIUM_RISK"),
    ("cases/test_suite/R009-blocked.yaml", "RULE-009", "RULE_009_BLOCKED"),
    # RULE-010
    ("cases/test_suite/R010-high.yaml", "RULE-010", "RULE_010_CULL_RECOMMENDED_HIGH"),
    ("cases/test_suite/R010-medium.yaml", "RULE-010", "RULE_010_CULL_RECOMMENDED_MEDIUM"),
    ("cases/test_suite/R010-blocked.yaml", "RULE-010", "RULE_010_BLOCKED"),
    ("cases/test_suite/R010-not-triggered.yaml", "RULE-010", "RULE_010_NOT_TRIGGERED"),
    # RULE-011
    ("cases/test_suite/R011-emergency.yaml", "RULE-011", "RULE_011_EMERGENCY"),
    ("cases/test_suite/R011-chronic.yaml", "RULE-011", "RULE_011_CHRONIC_CULL_CANDIDATE"),
    ("cases/test_suite/R011-targeted.yaml", "RULE-011", "RULE_011_TARGETED_TREATMENT"),
    ("cases/test_suite/R011-blind.yaml", "RULE-011", "RULE_011_BLIND_TREATMENT"),
    ("cases/test_suite/R011-monitor.yaml", "RULE-011", "RULE_011_MONITOR_CULTURE"),
    ("cases/test_suite/R011-not-app.yaml", "RULE-011", "RULE_011_NOT_APPLICABLE"),
    ("cases/test_suite/R011-blocked.yaml", "RULE-011", "RULE_011_BLOCKED"),
    # RULE-012
    ("cases/test_suite/R012-critical.yaml", "RULE-012", "RULE_012_CRITICAL_NEGATIVE"),
    ("cases/test_suite/R012-moderate.yaml", "RULE-012", "RULE_012_MODERATE_NEGATIVE"),
    ("cases/test_suite/R012-hyper.yaml", "RULE-012", "RULE_012_HYPERPRODUCTIVE_RISK"),
    ("cases/test_suite/R012-persistence.yaml", "RULE-012", "RULE_012_PERSISTENCE_ALERT"),
    ("cases/test_suite/R012-normal.yaml", "RULE-012", "RULE_012_WITHIN_RANGE"),
    ("cases/test_suite/R012-blocked.yaml", "RULE-012", "RULE_012_BLOCKED"),
]

RULE_MAP = {
    "RULE-001": rule_001,
    "RULE-002": rule_002,
    "RULE-003": rule_003,
    "RULE-004": rule_004,
    "RULE-005": rule_005,
    "RULE-006": rule_006,
    "RULE-007": rule_007,
    "RULE-008": rule_008,
    "RULE-009": rule_009,
    "RULE-010": rule_010,
    "RULE-011": rule_011,
    "RULE-012": rule_012,
}


def run():
    passed = 0
    failed = 0
    errors = []

    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + "  Rule Engine — Comprehensive Test Suite (12 Rules)  ".center(78) + "║")
    print("╚" + "═" * 78 + "╝")
    print()

    for path, rule_name, expected_verdict in TEST_CASES:
        case = load_yaml(path)
        attach_derived(case)
        module = RULE_MAP[rule_name]
        decision, prediction = module.evaluate(case)

        actual = decision.verdicts[0] if decision and decision.verdicts else "None"
        action = decision.action if decision else "None"
        ok = actual == expected_verdict

        status = "✅ PASS" if ok else "❌ FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
            errors.append((path, rule_name, expected_verdict, actual))

        conf = prediction.confidence.upper() if prediction and prediction.confidence else "—"
        print(f"{status}  {rule_name:<10} | {actual:<35} | {action:<40} | conf={conf:<6}  ({Path(path).name})")

    print()
    print("─" * 80)
    print(f"Результат: {passed} passed, {failed} failed  (всего {len(TEST_CASES)})")

    if errors:
        print()
        print("Ошибки:")
        for path, rule_name, expected, actual in errors:
            print(f"  • {rule_name} in {path}: ожидали {expected}, получили {actual}")
    else:
        print()
        print("🎉 Все тесты пройдены успешно!")

    print()
    return failed == 0


if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
