"""Abstract Base Class for portals"""
from abc import ABC
import asyncio
import logging
from typing import Any, Callable, Coroutine
from api.submission import Submission


class Portal(ABC):
    """Base class for all portals"""
    name = "Base"

    def __init__(self, on_receive: Callable[[Submission], Coroutine[Any, Any, str]]):
        """Function on_receive will be called whenever a new submission is detected"""
        self.on_receive = on_receive


class PassivePortal(Portal, ABC):
    """All passive portals should inherit from this class"""

    def __init__(self, on_receive: Callable[[Submission], Coroutine[Any, Any, str]]) -> None:
        """Function on_receive will be called whenever a new submission is detected"""
        logging.info("%s portal has been initialized", type(self).name)
        super().__init__(on_receive)

    async def start(self) -> None:
        """Start listening."""

class ActivePortal(Portal, ABC):
    """All active portals should inherit from this class"""

    def __init__(self, on_receive: Callable[[Submission], Coroutine[Any, Any, str]],
                 period: float) -> None:
        """Period is number of seconds to wait between crawling attempts"""
        logging.info(
            "%s portal has been initialized, crawling every %fs", type(self).name, period)
        super().__init__(on_receive)
        self.period = period

    async def crawl(self) -> None:
        """Should be implemented by subclasses. Simply starts crawling"""

    async def start(self) -> None:
        """Starts looping. This will call self.crawl periodically."""
        while True:
            self.crawl()
            asyncio.sleep(self.period)
