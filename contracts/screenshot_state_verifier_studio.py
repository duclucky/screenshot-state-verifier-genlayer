# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class ScreenshotStateVerifierStudio(gl.Contract):
    """Studio-ready deployable proof contract."""

    registry: str
    last_url: str
    last_claim: str
    last_expected_state: str
    last_result_json: str

    def __init__(self, initial_registry: str):
        self.registry = initial_registry
        self.last_url = ""
        self.last_claim = ""
        self.last_expected_state = ""
        self.last_result_json = ""

    @gl.public.view
    def get_registry(self) -> str:
        return self.registry

    @gl.public.view
    def get_last_verification(self) -> str:
        return self.last_result_json

    @gl.public.write
    def submit_visual_state_result(
        self,
        url: str,
        claim: str,
        expected_visual_state: str,
        result_json: str,
    ) -> None:
        self.last_url = url
        self.last_claim = claim
        self.last_expected_state = expected_visual_state
        self.last_result_json = result_json
        self.registry = "visual_state_result_registered"
