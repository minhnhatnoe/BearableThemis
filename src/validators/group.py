from typing import List
import logging
from validators import validatorabc
from src.api.submission import Submission

class Group(validatorabc.Validator):
    '''Bind multiple validators together'''
    name = "Group"
    def __init__(self, validators: List[validatorabc.Validator] = []):
        '''Simply assigns the validators'''
        self.validators = validators

    def __call__(self, sub: Submission) -> None:
        for validator in self.validators:
            validator(sub)

    def add(self, sub: Submission) -> None:
        for validator in self.validators:
            validator.add(sub)
