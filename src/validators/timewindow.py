import logging
import datetime
from validators import validatorabc
from src.api.submission import Submission

class TimeWindowError(validatorabc.CodeError):
    '''Thrown if submission is out of time window'''

class TimeWindow(validatorabc.Validator):
    '''Drop submissions that are out of '''
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        '''Simply assigns the validators'''
        self.start, self.end = start, end

    def __call__(self, sub: Submission) -> None:
        if self.start < sub.submit_timestamp and sub.submit_timestamp < self.end:
            return
        raise TimeWindowError("Code out of time window", "You are either too late or too soon")
