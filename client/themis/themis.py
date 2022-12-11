"""Helper classes to interact with Themis"""
import logging
from os import path
from . import fileio
from .submission import Submission

__all__ = ["ThemisInstance"]

class ThemisInstance:
    """The one and only object needed to interact with Themis."""

    def __init__(self, osd: str) -> None:
        """Initializes the instance with options.
            osd: Path set in Themis."""
        self.osd = osd
        if not path.exists(self.osd):
            raise FileNotFoundError(
                f"{self.osd} cannot be used because it doesn't exists.")
        logging.info("Created Instance writing to %s", self.osd)

    async def submit(self, sub: Submission) -> None|str:
        """Submits to Themis for judging. Returns the result if await_result is True"""
        fileio.submit(self.osd, sub)
        return await fileio.read_result(self.osd, sub)
