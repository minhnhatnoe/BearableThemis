from src.api import classes


class CodeError(Exception):
    '''Base class for throwing errors with codes submitted'''

    def __init__(self, console_msg: str, contestant_msg: str | None = None) -> None:
        '''Console_msg will be printed to console and log.\
           Contestant_msg will be sent to contestant, defaults to console_msg'''
        super().__init__()
        self.console_msg = console_msg
        self.contestant_msg = console_msg if contestant_msg is None else contestant_msg


class Validator:
    '''Base class for all validators. All validators should be derived from this class'''

    def __call__(self, sub: classes.Submission) -> None:
        '''Checks a submission'''

    def add(self, sub: classes.Submission) -> None:
        '''Mark a submission as added'''
