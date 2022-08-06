import asyncio
from os import path
from src import config
from src.api import classes


class FileIOException(Exception):
    '''Class for throwing exceptions around'''

def write_file(fpath: str, content: str) -> None:
    '''Write a file to a folder. Throws if file already exists.'''
    if path.exists(fpath):
        raise FileIOException(f"Duplicated file. Name: {fpath}")
    sanitized_code = content.encode("ascii", errors="ignore")
    with open(fpath, 'xb') as submit_file:
        submit_file.write(sanitized_code)

def submit(osd: str, sub: classes.Submission) -> None:
    '''Submit a submission. Make internal call to write_file.'''
    fname = sub.get_file_name()
    write_file(path.join(osd, fname), sub.content)

def read_log(fpath: str) -> str:
    with open(fpath, "r", encoding="utf-8") as file:
        return file.read()

async def read_result(osd: str, sub: classes.Submission) -> str:
    fname = sub.get_file_name(sub)
    log_file_path = path.join(osd, "logs", f"{fname}.log")
    for _ in range(config.RESULT_READ_TIMEOUT):
        if not path.exists(log_file_path):
            await asyncio.sleep(1)
        return read_log(log_file_path)
    raise FileIOException(f"Read {log_file_path} timed out after {config.RESULT_READ_TIMEOUT}s")
