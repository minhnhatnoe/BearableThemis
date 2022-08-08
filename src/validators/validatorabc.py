from abc import ABC
import logging
from typing import Type
from src.api.submission import Submission


class Validator(ABC):
    '''Base class for all validators. All validators should be derived from this class'''
    name = "Base"
    def __call__(self, sub: Submission) -> None:
        '''Checks a submission'''

    def add(self, sub: Submission) -> None:
        '''Mark a submission as added'''

class CodeError(Exception):
    '''Base class for throwing errors with codes submitted'''
    def __init__(self, validator_cls: Type[Validator], sub: Submission, detail: str) -> None:
        '''Make messages describing the failure in detail'''
        self.console_msg = \
            f"{validator_cls.name}: {sub.contestant}'s code of {sub.problem_name} - {detail}"
        logging.warning(self.console_msg)
        super().__init__(self.console_msg)
        self.contestant_msg = f"{validator_cls.name}: {detail}"
