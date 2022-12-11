"""Modules to control submission time window"""
import datetime
from ...themis.submission import Submission
from ..error import CodeError
from ..modules.validatorabc import Validator

__all__ = ["StartTime", "EndTime", "TimeWindow"]


class StartTime(Validator):
    """Drop submissions with submit_timestamp out of range [start, +inf)"""
    name = "StartTime"

    def __init__(self, start: datetime.datetime):
        """Start is the starting moment"""
        self.start = start

    def __call__(self, sub: Submission) -> None:
        if sub.submit_timestamp < self.start:
            detail = f"Submission made at {sub.submit_timestamp}, which is before {self.start}"
            raise CodeError(type(self), sub, detail)


class EndTime(Validator):
    """Drop submissions with submit_timestamp out of range (-inf, end)"""
    name = "EndTime"

    def __init__(self, end: datetime.datetime):
        """End is the ending moment"""
        self.end = end

    def __call__(self, sub: Submission) -> None:
        if sub.submit_timestamp >= self.end:
            detail = f"Submission made at {sub.submit_timestamp}, which is after {self.end}"
            raise CodeError(type(self), sub, detail)
