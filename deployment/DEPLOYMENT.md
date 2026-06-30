# Deployment

## Live GenLayer Deployment

Network: GenLayer Bradbury Testnet

Contract address: `0x7Dc8c7137606D2025a47579AebF0aDBf13a2F68C`

Deploy transaction hash: `0x31a73cd4a24643d1dee09dd5903b50bea94a082c7388a8f6ea334678092d1272`

Verification transaction hash: `0xf62320311b1b075a28e05bc3770c158776ba3ffe353f4aa56eb838f63691175d`

The successful deployment was completed through the GenLayer Studio UI on Bradbury Testnet.

Use `contracts/screenshot_state_verifier_studio.py` first.

Constructor input:

```text
Screenshot State Verifier registry initialized
```

Call:

```text
submit_visual_state_result(url, claim, expected_visual_state, result_json)
```

If Studio schema loading fails, use `contracts/screenshot_state_verifier_minimal_storage.py`.
