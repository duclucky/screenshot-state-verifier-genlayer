# GenLayer Intelligent Contract Submission

## Title

Screenshot State Verifier

## Category

Intelligent Contracts

## Summary

Screenshot State Verifier is a reusable GenLayer Intelligent Contract primitive for verifying whether a webpage or dApp UI visually matches a claimed state.

## Purpose

The contract helps builders verify visual evidence such as status pages, dashboards, dApp UI states, milestone pages, and audit screenshots.

## Consensus design

Validators should independently evaluate the same rendered screenshot and claim. The final verdict should be accepted when the material verdict is equivalent across validators. Material disagreement should return `ambiguous` or `requires_manual_review`.

## State design

The intended result stores:

```text
verification_id
url
claim
expected_visual_state
verdict
confidence
visual_evidence_summary
mismatch_reason
requires_manual_review
risk_flags
validator_equivalence_note
```

## Deployment placeholders

```text
Network:
Contract address:
Deploy transaction hash:
Verification transaction hash:
```

## Why this is not simple storage

The Studio fallback stores result JSON for deployment proof, but the actual submission is a reusable visual verification primitive with screenshot evaluation and validator-equivalence design.
