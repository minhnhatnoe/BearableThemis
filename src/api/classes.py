import datetime
import hashlib
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

class ThemisInstance:
    def __init__(self, osd: str, skip_duplicate: config.SKIP_DUPLICATE) -> None:
        '''The one and only object needed to interact with Themis.'''
        self.osd = osd
        self.skip_duplicate = skip_duplicate
        # TODO: Implement system to skip duplicate codes

    async def submit(self,
                     submission: Submission,
                     await_result: bool = config.ONLINE_MODE) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''
        fileio.submit(self.osd, submission)
        if not await_result:
            return None
