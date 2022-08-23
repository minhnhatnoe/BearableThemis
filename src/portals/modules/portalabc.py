"""Abstract Base Class for portals"""
from abc import ABC
from typing import AsyncGenerator
from api.submission import Submission

class Portal(ABC):
    def __init__(self) -> None:
        """Initializes the Portal with respective arguments"""

    async def listen(self) -> AsyncGenerator[Submission, None]:
        """Starts listening to codes. Overwrite for active portals."""
        while True:
            new_subs = self.manual_fetch()
            for subs in new_subs:
                yield subs
    
    def manual_fetch(self) -> list[Submission]:
        """Check source for code. Overwrite for passive portals."""
