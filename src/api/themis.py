'''Helper classes to interact with Themis'''
from os import path
import logging
import config
from api import fileio
from api.submission import Submission
from validators import Validator
from validators.error import CodeError

__all__ = ['ThemisInteractError', 'ThemisInstance']

class ThemisInteractError(Exception):
    '''Class for throwing Themis errors around'''

class ThemisInstance:
    '''The one and only object needed to interact with Themis.'''

    def __init__(self, work_path: str, validator: Validator,
                 await_result: bool = config.ONLINE_MODE) -> None:
        '''Initializes the instance with options.
        work_path: parent path of path set in Themis.
        validator: a validator that will throw subclasses of CodeError'''

        self.osd = str(path.join(work_path, "osd"))
        self.rejected = str(path.join(work_path, "rejected"))
        if not path.exists(self.osd):
            raise FileNotFoundError(
                f"{self.osd} cannot be used because it doesn't exists.")
        self.validator = validator
        self.await_result = await_result
        logging.info("Created Instance writing to %s", self.osd)

    def validate_submission(self, sub: Submission) -> None:
        '''Checks if a submission is legitimate'''
        self.validator(sub)

    async def submit(self, sub: Submission) -> None | str:
        '''Submits to Themis for judging. Returns the result if await_result is True'''
        try:
            self.validate_submission(sub)
        except CodeError:
            fileio.submit(self.rejected, sub)
        fileio.submit(self.osd, sub)
        self.validator.add(sub)
        if not self.await_result:
            return None
        return await fileio.read_result(self.osd, sub)
