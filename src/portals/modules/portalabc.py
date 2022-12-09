"""Abstract Base Class for portals"""
from abc import ABC
from api.submission import Submission


class Portal(ABC):
    """Base class for all portals. All portals should inherit this."""
    name = ""

    def __init__(self, jury: callable[Submission]) -> None:
        """Initializes the Portal with respective arguments"""
        self.jury = jury

    async def listen(self) -> None:
        """Listen for codes"""
