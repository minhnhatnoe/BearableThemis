"""A validator that ensures current """
from api.submission import Submission
from validators.error import CodeError
from validators.modules.validatorabc import Validator

__all__ = ["LastSubmit"]


class LastSubmit(Validator):
    """Ensures that only the last submission is taken into account"""
    name = "LastSubmit"

    def __init__(self):
        """Intializes the submission dict"""
        self.subs_time = {}

    def __call__(self, sub: Submission) -> None:
        """Checks if submission is truly last"""
        try:
            if sub.submit_timestamp < self.subs_time[sub.contestant][sub.problem_name]:
                detail = f"Code submitted at {self.subs_time[sub.contestant][sub.problem_name]} judged"
                raise CodeError(type(self), sub, detail)
        except KeyError:
            return

    def add(self, sub: Submission) -> None:
        """Add the submission"s timestamp"""
        if sub.contestant not in self.subs_time:
            self.subs_time[sub.contestant] = {}
        self.subs_time[sub.contestant][sub.problem_name] = sub.submit_timestamp
