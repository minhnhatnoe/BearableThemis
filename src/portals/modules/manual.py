"""Manual submission portal"""
from datetime import datetime
from typing import AsyncGenerator
from api import Submission
from portals.modules.portalabc import Portal


class ManualPortal(Portal):
    """Experimental portal, merely a placeholder.
    This should not be used in production."""
    name = "Manual"

    async def listen(self) -> AsyncGenerator[Submission, str]:
        """Waits for codes"""
        while True:
            name = input("Name: ")
            problem = input("Problem: ")
            code_path = input("Code_path: ")
            with open(code_path, "r", encoding="utf-8") as file:
                code = file.read()
            result = yield Submission(
                name, problem, "cpp", code, "manual", datetime.now())
            print(result)
