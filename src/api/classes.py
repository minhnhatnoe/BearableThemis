'''Helper classes to interact with Themis'''
from os import path
import logging
from typing import List
from src import config
from src.api import fileio
from src.api.submission import Submission
from validators import validbase

class ThemisInteractError(Exception):
    '''Class for throwing Themis errors around'''

class ThemisInstance:
    '''The one and only object needed to interact with Themis.'''

    def __init__(self, osd: str, contestants: List[str],
                 validators: validbase.Validator) -> None:
        '''Initializes the instance with options.
        OSD: path set in Themis.
        Contestants: list of contestant.
        Validators: list of validators that will throw subclasses of CodeError'''

        if not path.exists(osd):
            raise FileNotFoundError(
                f"{osd} cannot be used because it doesn't exists.")
        self.osd = osd
        self.contestants = {contestant for contestant in contestants}
        self.validators = validators
        logging.info(f"Created Instance writing to {self.osd}")

    def is_contestant(self, name: str) -> bool:
        '''Checks whether a name is a contestant of this instance'''
        return name in self.contestants

    def validate_submission(self, sub: Submission) -> None:
        '''Checks if a submission is legitimate'''
        if hash(sub.content) in self.contestants[sub.contestant]:
            logging.warning(
                f"{sub.contestant}'s code of {sub.problem_name} is duplicated.")
            raise validbase.DuplicatedCodeError("Duplicated code.", contestant_msg="You submitted duplicated code")
        for validator in self.validators:
            try:
                validator(sub)
            except validbase.CodeError as error:
                logging.warning(
                    f"Validator {validator.__name__} denied \
{sub.contestant}'s code of {sub.problem_name} due to {error.console_msg}")
                raise error

    async def submit(self,
                     sub: Submission,
                     await_result: bool = config.ONLINE_MODE) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''

        assert(self.is_contestant(sub.contestant))
        self.validate_sub(sub)
        fileio.submit(self.osd, sub)
        if not await_result:
            return None
        return await fileio.read_result(self.osd, sub)
