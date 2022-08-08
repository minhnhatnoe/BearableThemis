"""Abstract Base Class for portals"""
from abc import ABC
import logging
from typing import Callable, Coroutine
from src.api.submission import Submission


class Portal(ABC):
    """Base class for all portals"""
    name = "Base"

    def __init__(self, on_recieve: Callable[[Submission], Coroutine[None]]):
        """Function on_recieve will be called whenever a new submission is detected"""
        self.on_recieve = on_recieve


class PassivePortal(Portal, ABC):
    """All passive portals should inherit from this class"""

    def __init__(self, on_recieve: Callable[[Submission], Coroutine[None]]):
        """Function on_recieve will be called whenever a new submission is detected"""
        logging.info("%s portal has been initialized", type(self).name)
        super().__init__(on_recieve)


class ActivePortal(Portal, ABC):
    """All active portals should inherit from this class"""

    def __init__(self, on_recieve: Callable[[Submission], Coroutine[None]],
                 period: float):
        """Period is number of seconds to wait between crawling attempts"""
        logging.info(
            "%s portal has been initialized, crawling every %fs", type(self).name, period)
        super().__init__(on_recieve)
        self.period = period

    def crawl(self):
        """Should be implemented by subclasses. Simply starts crawling"""

    def start_loop(self):
        """Starts looping. This will call self.crawl periodically."""
        # TODO
