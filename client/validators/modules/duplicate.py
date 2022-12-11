"""Check if a submission is duplicated"""
from ...themis.submission import Submission
from ..error import CodeError
from ..modules.validatorabc import Validator

__all__ = ["Duplicate"]

class Duplicate(Validator):
    """Check if code is duplicated"""
    name = "Duplicate"

    def __init__(self) -> None:
        """Initializes the code hash dict"""
        self.code_hashes = {}

    def __call__(self, sub: Submission) -> None:
        """Check if submission already exists"""
        if sub.contestant not in self.code_hashes:
            return

        hash_val = hash(sub.content)
        if hash_val in self.code_hashes[sub.contestant]:
            detail = f"Similar code submitted at {self.code_hashes[sub.contestant][hash_val]}"
            raise CodeError(type(self), sub, detail)

    def add(self, sub: Submission) -> None:
        """Hashes and add the submission"""

        if sub.contestant not in self.code_hashes:
            self.code_hashes[sub.contestant] = {}

        self.code_hashes[sub.contestant][hash(sub.content)] = sub.submit_timestamp
