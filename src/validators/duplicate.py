from validators import validatorabc
from src.api.submission import Submission


class Duplicate(validatorabc.Validator):
    '''Check if code is duplicated'''
    name = "Duplicate"

    def __init__(self) -> None:
        '''Initializes the code hash dict'''
        self.code_hashes = {}

    def __call__(self, sub: Submission) -> None:
        '''Check if submission already exists'''
        if sub.contestant not in self.code_hashes:
            return

        hash_val = hash(sub.content)
        if hash_val in self.code_hashes[sub.contestant]:
            detail = f"Same code submitted at {self.code_hashes[sub.contestant][hash_val]}"
            raise validatorabc.CodeError(type(self), sub, detail)

    def add(self, sub: Submission) -> None:
        '''Hashes and add the submission'''

        if sub.contestant not in self.code_hashes:
            self.code_hashes[sub.contestant] = {}

        self.code_hashes[sub.contestant][hash(sub.content)] = sub.submit_timestamp
