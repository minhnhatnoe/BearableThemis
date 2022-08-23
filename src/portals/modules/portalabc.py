"""Abstract Base Class for portals"""
from abc import ABC
import asyncio
from typing import AsyncGenerator
from api.submission import Submission

class Portal(ABC):
    def __init__(self) -> None:
        """Initializes the Portal with respective arguments"""

    async def listen(self) -> AsyncGenerator[Submission, str]:
        """Starts listening to codes. Overwrite for passive portals."""
        while True:
            new_subs = await self.manual_fetch()
            for subs in new_subs:
                result = yield subs
            await asyncio.sleep(0.5)
    
    async def manual_fetch(self) -> list[Submission]:
        """Check source for code. Overwrite for active portals."""
