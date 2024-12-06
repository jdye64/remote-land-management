import logging

logger = logging.getLogger(__name__)


class Runner:
    """Driver to run the actual space planning application"""

    def __init__(self, run_mode: str, assets_file: str):
        self._run_mode = run_mode
        self._assets_file = assets_file
        print("Initializing Runner with run mode: %s", run_mode)

    def invoke(self):
        """Invoke the runner"""
        print("Running planner ....")
        return True
