'''Contains ABC for validators'''
from abc import ABC
from src.api.submission import Submission
__all__ = ['Validator']

class Validator(ABC):
    '''Base class for all validators. All validators should be derived from this class'''
    name = "Base"
    def __call__(self, sub: Submission) -> None:
        '''Checks a submission'''

    def add(self, sub: Submission) -> None:
        '''Mark a submission as added'''
