"""Abstract Base Class for portals"""
from abc import ABC
import asyncio
from typing import AsyncGenerator
from api.submission import Submission

class Portal(ABC):
    def __init__(self) -> None:
        """Initializes the Portal with respective arguments"""

    async def listen(self) -> AsyncGenerator[Submission, str]:
        """Starts listening to codes."""
