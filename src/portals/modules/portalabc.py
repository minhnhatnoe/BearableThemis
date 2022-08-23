"""Abstract Base Class for portals"""
from abc import ABC
from typing import AsyncGenerator
from api.submission import Submission

class Portal(ABC):
    """Base class for all portals. All portals should inherit this."""
    def __init__(self) -> None:
        """Initializes the Portal with respective arguments"""

    async def listen(self) -> AsyncGenerator[Submission, str]:
        """Starts listening to codes."""
