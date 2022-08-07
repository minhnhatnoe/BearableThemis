from typing import List
import logging
from validators import validatorabc
from src.api.submission import Submission

class Sequential(validatorabc.Validator):
    '''Bind multiple validators together'''
    def __init__(self, validators: List[validatorabc.Validator] = []):
        '''Simply assigns the validators'''
        self.validators = validators
    
    def __call__(self, sub: Submission) -> None:
        for validator in self.validators:
            try: 
                validator(sub)
            except validatorabc.CodeError as exception:
                logging.warning(f"Sequential validator failed at {validator.__class__.__name__}")
                raise exception
    
    def add(self, sub: Submission) -> None:
        for validator in self.validators:
            validator.add(sub)
