'''Helper classes to interact with Themis'''
from os import path
import logging
from typing import List
import config
from api import fileio
from api.submission import Submission
from validators import Validator

__all__ = ['ThemisInteractError', 'ThemisInstance']

class ThemisInteractError(Exception):
    '''Class for throwing Themis errors around'''

class ThemisInstance:
    '''The one and only object needed to interact with Themis.'''

    def __init__(self, osd: str, contestants: List[str],
                 validator: Validator,
                 await_result: bool = config.ONLINE_MODE) -> None:
        '''Initializes the instance with options.
        OSD: path set in Themis.
        Contestants: list of contestant.
        Validators: list of validators that will throw subclasses of CodeError'''

        if not path.exists(osd):
            raise FileNotFoundError(
                f"{osd} cannot be used because it doesn't exists.")
        self.osd = osd
        self.contestants = set(contestants)
        self.validator = validator
        self.await_result = await_result
        logging.info("Created Instance writing to %s", self.osd)

    def is_contestant(self, name: str) -> bool:
        '''Checks whether a name is a contestant of this instance'''
        return name in self.contestants

    def validate_submission(self, sub: Submission) -> None:
        '''Checks if a submission is legitimate'''
        self.validator(sub)

    async def submit(self, sub: Submission) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''

        assert self.is_contestant(sub.contestant)
        self.validate_submission(sub)
        fileio.submit(self.osd, sub)
        self.validator.add(sub)
        if not self.await_result:
            return None
        return await fileio.read_result(self.osd, sub)
