import datetime
from src import config

class ThemisInstance:
    def __init__(self, osd: str) -> None:
        self.osd = osd

class Submission:
    def __init__(self, lang: str, contestant: str, problem_name: str,
                source: str,
                submit_timestamp: datetime.datetime,
                recieve_timestamp: datetime.datetime = datetime.datetime.now()) -> None:
        '''Creates a new submission.
        Lang: extension of code.
        Source: Information regarding source of submission.
        Submit_timestamp: Timestamp retrieved from the respective service'''
        self.lang, self.contestant, self.problem_name = lang, contestant, problem_name
        self.source = source
        self.submit_timestamp, self.recieve_timestamp = submit_timestamp, recieve_timestamp

    async def submit(await_result: bool = config.ONLINE_MODE) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''

