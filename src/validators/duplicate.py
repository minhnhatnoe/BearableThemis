from src.validators import validbase
from src.api.submission import Submission


class DuplicatedCodeError(validbase.CodeError):
    '''Class for throwing when code is duplicated'''


class Duplicate:
    '''Check if code is duplicated'''

    def __init__(self):
        '''Initializes the code hash dict'''
        self.code_hashes = {}

    def __call__(self, sub: Submission):
        '''Check if submission already exists'''

    def add(self, sub: Submission):
        '''Hashes and add the submission'''
