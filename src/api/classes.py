from os import path
import logging
import datetime
import hashlib
from typing import List
from src import config
from src.api import fileio

class Submission:
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
        logging.info(f"Recieved {problem_name}.{lang} of {contestant} from {source} at {recieve_timestamp}")
    
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
    '''Class for throwing errors with codes submitted'''

class BannedSyntax(CodeError):
    '''Thrown if specified pattern appears in code'''

class DuplicatedCodeError(CodeError):
    '''Thrown if user submitted duplicate code'''

class ThemisInstance:
    def __init__(self, osd: str, contestants: List[str],
                 skip_duplicate: config.SKIP_DUPLICATE) -> None:
        '''The one and only object needed to interact with Themis.'''
        if not path.exists(osd):
            raise FileNotFoundError(f"{osd} cannot be used because it doesn't exists.")
        self.osd = osd
        self.skip_duplicate = skip_duplicate
        self.contestants = {contestant: {} for contestant in contestants}
        logging.info(f"Created Instance writing to {self.osd}")
    
    def is_contestant(self, name: str) -> bool:
        return name in self.contestants

    def submission_legit(self, submission: Submission) -> None:
        if hash(submission.content) in self.contestants[submission.contestant]:
            raise CodeError("Duplicated code")
        
    
    async def submit(self,
                     submission: Submission,
                     await_result: bool = config.ONLINE_MODE) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''

        fileio.submit(self.osd, submission)
        if not await_result: return None
        return await fileio.read_result(self.osd, submission)
