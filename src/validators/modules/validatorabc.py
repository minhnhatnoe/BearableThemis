"""Contains ABC for validators"""
from abc import ABC
from api.submission import Submission
__all__ = ["Validator"]

class Validator(ABC):
    """Base class for all validators. All validators should be derived from this class"""
    name = "Base"
    def __init__(self, *args) -> None:
        """Initializes code validator."""

    def __call__(self, sub: Submission) -> None:
        """Checks a submission"""

    def add(self, sub: Submission) -> None:
        """Mark a submission as added"""
