"""Functions to interact with Themis"""
import asyncio
from os import path
import config
from api.submission import Submission

class FileIOException(Exception):
    """Class for throwing exceptions around"""

def write_file(fpath: str, content: str) -> None:
    """Write a file to a folder. Throws if file already exists."""
    if path.exists(fpath):
        raise FileIOException(f"Duplicated file. Name: {fpath}")
    sanitized_code = content.encode("utf-8", errors="ignore")
    with open(fpath, "xb") as submit_file:
        submit_file.write(sanitized_code)

def submit(osd: str, sub: Submission) -> None:
    """Submit a submission. Make internal call to write_file."""
    fname = sub.get_file_name()
    write_file(path.join(osd, fname), sub.content)

def read_log(fpath: str) -> str:
    """Reads a utf-8 text file"""
    with open(fpath, "r", encoding="utf-8") as file:
        return file.read()

async def read_result(osd: str, sub: Submission) -> str:
    """Waits for judge to finish, then reads the resulting log file"""
    fname = sub.get_file_name()
    log_file_path = path.join(osd, "Logs", f"{fname}.log")
    for _ in range(config.RESULT_READ_TIMEOUT):
        if path.exists(log_file_path):
            return read_log(log_file_path)
        await asyncio.sleep(1)
    raise FileIOException(f"Read {log_file_path} timed out after {config.RESULT_READ_TIMEOUT}s")
