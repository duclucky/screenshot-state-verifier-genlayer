# Screenshot State Verifier

Screenshot State Verifier is a standalone GenLayer Intelligent Contract submission. It verifies whether a webpage or dApp UI visually matches a claimed state.

This is not a webapp. It is a reusable Intelligent Contract primitive for builders who need visual evidence verification.

## Core idea

Input:

```text
url
claim
expected_visual_state
verification_policy
```

Intended flow:

```text
render webpage screenshot
→ evaluate screenshot against the claim
→ produce a structured verdict
→ validators independently re-run the evaluation
→ compare the results for equivalence
→ store a verification record
```

## Verdicts

```text
verified
not_verified
ambiguous
page_unavailable
requires_manual_review
```

## Repository structure

```text
contracts/
  screenshot_state_verifier.py
  screenshot_state_verifier_studio.py
  screenshot_state_verifier_minimal_storage.py
examples/
  status_page_claim.json
  dapp_ui_claim.json
  ambiguous_claim.json
  expected_outputs.json
tests/
  test_result_schema.py
  test_verification_policy.py
deployment/
  DEPLOYMENT.md
  deployment_info.example.json
  deployment_info.json
```

## Live GenLayer Deployment

Network: GenLayer Bradbury Testnet

Contract address: `0x7Dc8c7137606D2025a47579AebF0aDBf13a2F68C`

Deploy transaction hash: `0x31a73cd4a24643d1dee09dd5903b50bea94a082c7388a8f6ea334678092d1272`

Verification transaction hash: `0xf62320311b1b075a28e05bc3770c158776ba3ffe353f4aa56eb838f63691175d`

The successful deployment was completed through the GenLayer Studio UI on Bradbury Testnet.

## Local tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## GenLayer Studio deployment path

1. Open GenLayer Studio.
2. Create a new contract file.
3. Paste `contracts/screenshot_state_verifier_studio.py`.
4. Deploy on GenLayer Bradbury Testnet.
5. Record network, contract address, deploy transaction hash, and verification transaction hash.
6. Update `deployment/deployment_info.json`.

## Why this matters

Visual state verification is useful for status pages, dApp dashboards, dashboard state verification, milestone proof verification, audit screenshots, and visual dispute evidence.

The value is not simple storage. The primitive is the combination of visual evidence, a claim, a policy, validator review, and a structured verdict.
