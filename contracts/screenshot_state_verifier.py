"""Screenshot State Verifier.

Main intended GenLayer Intelligent Contract primitive.

This file documents the full contract boundary for visual webpage/UI state
verification. Runtime APIs for screenshot rendering and image inputs should be
aligned with the currently supported GenLayer SDK/Studio version before
production deployment.
"""

from genlayer import *


class ScreenshotStateVerifier(gl.Contract):
    """Verify whether a webpage screenshot matches a claimed visual state."""

    last_verification: str
    verification_count: int

    def __init__(self):
        self.last_verification = ""
        self.verification_count = 0

    @gl.public.write
    def verify_webpage_state(
        self,
        url: str,
        claim: str,
        expected_visual_state: str,
        verification_policy: str,
    ) -> None:
        """Verify a webpage state from visual evidence.

        Intended GenLayer runtime pattern:
        1. Render a screenshot from `url`.
        2. Send screenshot + claim + expected state to a vision-capable model.
        3. Request a strict JSON response.
        4. Validators independently re-run the evaluation.
        5. Apply equivalence/consensus checks.

        Pseudocode shape:
        screenshot = gl.nondet.web.render(url, mode="screenshot")
        model_result = gl.nondet.llm(prompt, images=[screenshot], response_format="json")
        accepted = gl.eq_principle.strict_eq(model_result)
        """
        self.verification_count += 1
        verification_id = "verification_" + str(self.verification_count)
        esc = lambda s: s.replace('\', '\\').replace('"', '\"')
        result_json = (
            "{"
            + '"verification_id":"' + verification_id + '",'
            + '"url":"' + esc(url) + '",'
            + '"claim":"' + esc(claim) + '",'
            + '"expected_visual_state":"' + esc(expected_visual_state) + '",'
            + '"verdict":"requires_manual_review",'
            + '"confidence":"unknown",'
            + '"visual_evidence_summary":"Runtime screenshot evaluation should populate this field.",'
            + '"mismatch_reason":"Not evaluated in placeholder path.",'
            + '"requires_manual_review":true,'
            + '"risk_flags":["runtime_evaluation_required"],'
            + '"validator_equivalence_note":"Consensus evaluation should be performed by validators."'
            + "}"
        )
        self.last_verification = result_json

    @gl.public.view
    def get_last_verification(self) -> str:
        return self.last_verification

    @gl.public.view
    def get_verification_count(self) -> int:
        return self.verification_count

    @gl.public.view
    def get_verification_by_id(self, verification_id: str) -> str:
        if verification_id == "latest":
            return self.last_verification
        return ""
