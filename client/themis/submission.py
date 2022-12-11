"""Contains the Submission class"""
import logging
import datetime
from dataclasses import dataclass

__all__ = ["Submission", "available_langs"]
available_langs = ["cpp", "py"]

@dataclass(frozen=True, slots=True)
class Submission:
    """Represents a submission.

    Args:
        contestant (str): ID of contestant.
        problem_name (str): ID of problem.
        lang (str): Extension of the code (without the ".").
        content (str): Content of the code.
        source (str): Information regarding where the code was gotten from.
        submit_timestamp (datetime.datetime): Timestamp from the source.
    """
    contestant: str
    problem_name: str
    lang: str
    content: str
    origin: str
    submit_timestamp: datetime.datetime

    def __post_init__(self) -> None:
        """Creates a new submission.
        lang: extension of code.
        origin: Information regarding origin of submission.
        submit_timestamp: Timestamp retrieved from the respective service"""
        logging.info("Received %s.%s of %s from %s at %s",
            self.problem_name, self.lang, self.contestant, self.origin, self.submit_timestamp)
        assert self.lang in available_langs

    def get_file_name(self) -> str:
        """Generate file name when interacting with themis"""
        hash_val = f"{hash(self):X}"
        return f"{hash_val[-8:]}[{self.contestant}][{self.problem_name}].{self.lang}"
