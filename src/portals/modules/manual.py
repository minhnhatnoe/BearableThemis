"""Manual submission portal"""
from datetime import datetime
from api import Submission
from portals.modules.portalabc import PassivePortal

class ManualPortal(PassivePortal):
    """Experimental portal, merely a placeholder.
    This should not be used in production."""
    name = "manual"

    async def start(self) -> None:
        while True:
            name = input("Name: ")
            problem = input("Problem: ")
            code_path = input("Code_path: ")
            with open(code_path, "r", encoding="utf-8") as file:
                code = file.read()
            result = await self.on_receive(
                Submission(name, problem, "cpp", code,
                           "manual", datetime.now()))
            print(result)
            
