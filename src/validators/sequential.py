from typing import List
import logging
from src.validators import validbase
from src.api.submission import Submission

class Sequential(validbase.Validator):
    '''Bind multiple validators together'''
    def __init__(self, validators: List[validbase.Validator] = []):
        '''Simply assigns the validators'''
        self.validators = validators
    
    def __call__(self, sub: Submission) -> None:
        for validator in self.validators:
            try: 
                validator(sub)
            except validbase.CodeError as exception:
                logging.warning(f"Sequential validator failed at {validator.__class__.__name__}")
                raise exception
    
    def add(self, sub: Submission) -> None:
        for validator in self.validators:
            validator.add(sub)