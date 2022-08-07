'''Helper classes to interact with Themis'''
from os import path
import logging
from typing import List
from src import config
from src.api import fileio
from src.api.submission import Submission
from src.validators import validbase

class ThemisInteractError(Exception):
    '''Class for throwing Themis errors around'''

class ThemisInstance:
    '''The one and only object needed to interact with Themis.'''

    def __init__(self, osd: str, contestants: List[str],
                 validator: validbase.Validator) -> None:
        '''Initializes the instance with options.
        OSD: path set in Themis.
        Contestants: list of contestant.
        Validators: list of validators that will throw subclasses of CodeError'''

        if not path.exists(osd):
            raise FileNotFoundError(
                f"{osd} cannot be used because it doesn't exists.")
        self.osd = osd
        self.contestants = {contestant for contestant in contestants}
        self.validator = validator
        logging.info(f"Created Instance writing to {self.osd}")

    def is_contestant(self, name: str) -> bool:
        '''Checks whether a name is a contestant of this instance'''
        return name in self.contestants

    def validate_submission(self, sub: Submission) -> None:
        '''Checks if a submission is legitimate'''
        self.validator(sub)

    async def submit(self,
                     sub: Submission,
                     await_result: bool = config.ONLINE_MODE) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''

        assert(self.is_contestant(sub.contestant))
        self.validate_submission(sub)
        fileio.submit(self.osd, sub)
        if not await_result:
            return None
        return await fileio.read_result(self.osd, sub)
