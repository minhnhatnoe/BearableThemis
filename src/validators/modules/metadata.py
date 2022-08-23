'''Validator to check if metadata fits a contest'''
from api.submission import Submission
from validators.modules.validatorabc import Validator
from validators.error import CodeError

class Contestant(Validator):
    '''Checks if contestant is of contest'''
    name = "Contestant"

    def __init__(self, contestants: list[str]):
        '''Start is the starting moment'''
        self.contestants = set(contestants)

    def __call__(self, sub: Submission) -> None:
        if sub.contestant not in self.contestants:
            detail = f"User {sub.contestant} not in list of contestants"
            raise CodeError(type(self), sub, detail)

class Problems(Validator):
    '''Drop submissions with wrong problem id'''
    def __init__(self, problem_ids: list[str]):
        '''Start is the starting moment'''
        self.ids = set(problem_ids)

    def __call__(self, sub: Submission) -> None:
        if sub.problem_name not in self.ids:
            detail = f"Problem {sub.problem_name} not in this contest"
            raise CodeError(type(self), sub, detail)
