"""Functions to interact with Themis"""
import asyncio
from os import path
from .submission import Submission

RESULT_READ_TIMEOUT = 1000

class ThemisInteractError(Exception):
    """Class for throwing Themis errors around"""


def write_file(fpath: str, content: str) -> None:
    """Write a file to a folder. Throws if file already exists."""
    if path.exists(fpath):
        raise ThemisInteractError(f"Duplicated file. Name: {fpath}")
    sanitized_code = content.encode("utf-8", errors="ignore")
    with open(fpath, "xb") as submit_file:
        submit_file.write(sanitized_code)


def submit(osd: str, sub: Submission) -> None:
    """Submit a submission. Make internal call to write_file."""
    fname = sub.get_file_name()
    write_file(path.join(osd, fname), sub.content)


async def read_result(osd: str, sub: Submission) -> str:
    """Waits for judge to finish, then reads the resulting log file"""
    fname = sub.get_file_name()
    log_file_path = path.join(osd, "Logs", f"{fname}.log")
    for _ in range(RESULT_READ_TIMEOUT):
        if not path.exists(log_file_path):
            await asyncio.sleep(1)
        with open(log_file_path, "r", encoding="utf-8") as file:
            return file.read()
    raise ThemisInteractError(
        f"Read {log_file_path} timed out after {RESULT_READ_TIMEOUT}s")
