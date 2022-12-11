"""Manual submission portal"""
from datetime import datetime
from ..themis import Submission
from .portalabc import Portal


class ManualPortal(Portal):
    """Experimental portal, merely a placeholder.
    This should not be used in production."""
    name = "Manual"

    async def listen(self) -> None:
        """Waits for codes"""
        while True:
            name = input("Name: ")
            problem = input("Problem: ")
            code_path = input("Code_path: ")
            with open(code_path, "r", encoding="utf-8") as file:
                code = file.read()
            result = await self.judge(Submission(
                name, problem, "cpp", code, "manual", datetime.now()))
            print(result)
