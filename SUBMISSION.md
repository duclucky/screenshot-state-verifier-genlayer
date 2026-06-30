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

## Live GenLayer Deployment

```text
Network: GenLayer Bradbury Testnet
Contract address: 0x7Dc8c7137606D2025a47579AebF0aDBf13a2F68C
Deploy transaction hash: 0x31a73cd4a24643d1dee09dd5903b50bea94a082c7388a8f6ea334678092d1272
Verification transaction hash: 0xf62320311b1b075a28e05bc3770c158776ba3ffe353f4aa56eb838f63691175d
```

The successful deployment was completed through the GenLayer Studio UI on Bradbury Testnet.

## Why this is not simple storage

The Studio fallback stores result JSON for deployment proof, but the actual submission is a reusable visual verification primitive with screenshot evaluation and validator-equivalence design.
