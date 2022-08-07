import logging
import datetime
import hashlib


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

    def hash(self) -> str:
        '''Hashes a submission.
        The same submission from a platform (ie. Same cell in Sheets)\
        is guaranteed to have the same hash value across all runs.
        Internally, this uses sha256, and returns the first 8 characters'''
        box = hashlib.new("sha256")
        for data in [self.contestant, self.problem_name, self.lang,
                     self.content, self.source,
                     self.submit_timestamp]:
            box.update(bytes(f"{data}", 'utf-8'))
        return box.hexdigest()[:8]

    def get_file_name(self) -> str:
        return f"{self.hash()}[{self.contestant}][{self.problem_name}].{self.lang}"
