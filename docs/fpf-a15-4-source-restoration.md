---
type: fpf-study
pattern: A.15.4
title: "Work-Relevant Source Restoration: видимый артефакт ≠ разрешение"
domain: cattle-science
difficulty: intermediate
reading_time: 25 min
created: 2026-06-19
---

# A.15.4 — Work-Relevant Source Restoration

## 1. Зачем это читать

Dashboard показывает зелёную плитку «approved», credential badge говорит «valid», generated summary пишет «authorized». Команды спешат действовать, но визуальный cue — не source relation. A.15.4 учит восстанавливать несущий claim source, прежде чем полагаться на видимый артефакт.

**FPF-тезис:** *«Плитка не является gate decision. Badge не является role currentness. Summary не является evidence.»*

---

## 2. Когда применять

- dashboard tile выглядит как разрешение/доказательство;
- copied approval / review summary используется как authority;
- credential view / status register excerpt;
- generated explanation утверждает «authorized»;
- schema/API wording («allowed», «approved») ведёт к действию;
- composed source chain — несколько transform steps.

---

## 3. Минимальная source-restoration note

```text
SourceRestorationNote:
  EncounteredSourceCandidate:   green dashboard tile «Release approved»
  WorkOrRelianceClaimUnderRepair: deploy new feed ration
  ClaimOrEffectNeeded:          gate passage for production deployment
  GoverningSourceNeeded:        A.21 GateDecision + DecisionLogRef
  RelationGovernedMoveNow:      block deployment until source recovered
  BlockedOverread:              tile color ≠ gate passage
  StopOrReopenCondition:        recover GateDecisionRef, gate version, scope, window
```

---

## 4. Governing-source lookup

| Требуемый claim/effect | Источник |
|---|---|
| Approval / authorization / delegation | `A.2.9` SpeechActRef |
| Deontic permission / obligation | `A.2.8` Commitment |
| Role / status reliance | `A.2.1` RoleAssignment / credential proof / GateDecision |
| Gate passage | `A.21` GateDecision / DecisionLogRef |
| Constraint validity | `A.20` ConstraintValidity witness |
| Evidence / provenance | `A.10` evidence path |
| Assurance / readiness | `B.3` typed assurance claim |
| Work occurrence | `A.15.1` dated U.Work |

---

## 5. Dispositions

| Disposition | Когда |
|---|---|
| **Orientation / source-finding** | candidate — только publication face/cue |
| **Routine reliance** | bounded claim, source reference recoverable, нет high-impact |
| **High-impact reliance disposition** | safety, release, compliance, delegated, contested, cross-context — требуется полный governing source |

---

## 6. Фермерские примеры

### 6.1 Dashboard «BHB в норме»

- Encountered: dashboard tile green
- Claim needed: «коровы готовы к переводу на пастбище»
- Governing source: StateAssertion checklist over CharacteristicSpace + evidence path
- Blocked overread: цвет плитки ≠ state assertion

### 6.2 Copied approval in chat

- Encountered: «согласовано» в пересланном сообщении
- Claim needed: permission to buy equipment
- Governing source: A.2.9 SpeechActRef с actor, role, affected target, window
- Blocked overread: copy ≠ original speech act

### 6.3 Credential badge «certified veterinarian»

- Encountered: badge
- Claim needed: role currentness
- Governing source: issuer/trust root, status register, holder binding, freshness, revocation
- Blocked overread: badge ≠ permission to perform specific Work

---

## 7. Контрольный чеклист

- `CC-A.15.4.1`: видимый source candidate не заменяет governing source.
- `CC-A.15.4.2`: назван work/reliance claim under repair.
- `CC-A.15.4.3`: указан claim/effect, который должен нести source.
- `CC-A.15.4.4`: указан governing source по FPF kind и reference.
- `CC-A.15.4.5`: выбран lightest relation-governed move (orient/probe/block).
- `CC-A.15.4.6`: для high-impact claims — полный source и evidence path.
- `CC-A.15.4.7`: conflicting sources не разрешаются по цвету/салience/recency.

---

## 8. Связи

- **A.15.1 U.Work** — performed work source.
- **A.21 Operational Gate** — gate decisions.
- **A.2.9 SpeechAct** — issuing/approval acts.
- **A.2.8 Commitment** — deontic relations.
- **A.10 Evidence Graph Referring** — evidence paths.
- **B.3 Trust Framework** — assurance thresholds.
- **E.17 MVPK / generated explanations** — publication-face overread.

---

*Capture написан по FPF-Spec.md §A.15.4 для PACK-cattle-science.*
