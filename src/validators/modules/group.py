'''A validator that is a group of other validators'''
from typing import List
from src.validators.modules.validatorabc import Validator
from src.api.submission import Submission

__all__ = ['Group']


class Group(Validator):
    '''Bind multiple validators together'''
    name = "Group"

    def __init__(self, validators: List[Validator] | None):
        '''Simply assigns the validators'''
        self.validators = validators
        if validators is None:
            self.validators = []

    def __call__(self, sub: Submission) -> None:
        for validator in self.validators:
            validator(sub)

    def add(self, sub: Submission) -> None:
        for validator in self.validators:
            validator.add(sub)
