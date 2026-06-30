# Deployment

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
