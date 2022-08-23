'''Contains class for throwing errors related to submissions'''
import logging
from typing import Type
from validators.modules.validatorabc import Validator
from api.submission import Submission

__all__ = ['CodeError']


class CodeError(Exception):
    '''Class for throwing errors with codes submitted'''

    def __init__(self, validator_cls: Type[Validator], sub: Submission,
                 detail: str, continue_try: bool = False) -> None:
        '''Make messages describing the failure in detail'''
        self.console_msg = \
            f"{validator_cls.name}: {sub.contestant}'s code of {sub.problem_name} - {detail}"
        logging.warning(self.console_msg)
        super().__init__(self.console_msg)

        self.contestant_msg = f"{validator_cls.name}: {detail}"
        # If this error is just a check, and chances are contestant did nothing wrong
        self.continue_try = continue_try
