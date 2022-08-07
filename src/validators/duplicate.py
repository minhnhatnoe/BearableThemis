import logging
from src.validators import validbase
from src.api.submission import Submission


class DuplicatedCodeError(validbase.CodeError):
    '''Class for throwing when code is duplicated'''


class Duplicate(validbase.Validator):
    '''Check if code is duplicated'''

    def __init__(self) -> None:
        '''Initializes the code hash dict'''
        self.code_hashes = {}

    def __call__(self, sub: Submission) -> None:
        '''Check if submission already exists'''
        if sub.contestant not in self.code_hashes: return
        hash_val = hash(sub.content)
        if hash_val in self.code_hashes[sub.contestant]:
            logging.warning(
                f"{sub.contestant}'s code of {sub.problem_name} is duplicated.")
            raise validbase.DuplicatedCodeError("Duplicated code", "You submitted duplicated code")


    def add(self, sub: Submission) -> None:
        '''Hashes and add the submission'''
        self.code_hashes[sub.contestant].append(hash(sub.content))
