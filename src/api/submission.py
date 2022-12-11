"""Contains the Submission class"""
from dataclasses import dataclass, field
import logging
import datetime

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
        receive_timestamp (datetime.datetime): Timestamp of received moment.
    """
    contestant: str
    problem_name: str
    lang: str
    content: str
    source: str
    submit_timestamp: datetime.datetime
    receive_timestamp: datetime.datetime = field(
        default_factory=datetime.datetime.now, compare=False)

    def __post_init__(self) -> None:
        """Creates a new submission.
        Lang: extension of code.
        Source: Information regarding source of submission.
        Submit_timestamp: Timestamp retrieved from the respective service"""
        logging.info(
            "Recieved %s.%s of %s from %s at %s",
            self.problem_name, self.lang, self.contestant, self.source, self.receive_timestamp)
        assert self.lang in available_langs

    def get_file_name(self) -> str:
        """Generate file name when interacting with themis"""
        hash_val = f"{hash(self):X}"
        hash_val = hash_val[-8:]
        return f"{hash_val}[{self.contestant}][{self.problem_name}].{self.lang}"
