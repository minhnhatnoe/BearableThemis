'''Helper classes to interact with Themis'''
from os import path
import logging
import datetime
import hashlib
from typing import Callable, List
from src import config
from src.api import fileio


class Submission:
    '''Represents a submission'''
    def __init__(self, contestant: str, problem_name: str, lang: str,
                 content: str, source: str,
                 submit_timestamp: datetime.datetime,
                 recieve_timestamp: datetime.datetime = datetime.datetime.now()) -> None:
        '''Creates a new submission.
        Lang: extension of code.
        Source: Information regarding source of submission.
        Submit_timestamp: Timestamp retrieved from the respective service'''
        self.contestant, self.problem_name, self.lang = contestant, problem_name, lang
        self.content = content
        self.source = source
        self.submit_timestamp, self.recieve_timestamp = submit_timestamp, recieve_timestamp
        logging.info(
            f"Recieved {problem_name}.{lang} of {contestant} from {source} at {recieve_timestamp}")

    def __hash__(self) -> str:
        '''Hashes a submission.
        The same submission from a platform (ie. Same cell in Sheets)\
        is guaranteed to have the same hash value across all runs.
        Internally, this uses sha256, and returns the first 8 characters'''
        box = hashlib.new("sha256")
        for data in [self.contestant, self.problem_name, self.lang,
                     self.content, self.source,
                     self.submit_timestamp]:
            box.update(bytes(data))
        return box.hexdigest()[:8]

    def get_file_name(self) -> str:
        return f"{hash(self)}[{self.contestant}][{self.problem_name}].[{self.lang}]"


class ThemisInteractError(Exception):
    '''Class for throwing Themis errors around'''


class CodeError(Exception):
    '''Base class for throwing errors with codes submitted'''

    def __init__(self, console_msg: str, contestant_msg: str|None = None) -> None:
        '''Console_msg will be printed to console and log.\
           Contestant_msg will be sent to contestant, defaults to console_msg'''
        super().__init__()
        self.console_msg = console_msg
        self.contestant_msg = console_msg if contestant_msg is None else contestant_msg


class DuplicatedCodeError(CodeError):
    '''Class for throwing when code is duplicated'''


class ThemisInstance:
    '''The one and only object needed to interact with Themis.'''

    def __init__(self, osd: str, contestants: List[str],
                 validators: List[Callable[[Submission], None]]) -> None:
        '''Initializes the instance with options'''
        if not path.exists(osd):
            raise FileNotFoundError(
                f"{osd} cannot be used because it doesn't exists.")
        self.osd = osd
        self.contestants = {contestant: {} for contestant in contestants}
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
            raise DuplicatedCodeError("Duplicated code.", contestant_msg="You submitted duplicated code")
        for validator in self.validators:
            try:
                validator(sub)
            except CodeError as error:
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
