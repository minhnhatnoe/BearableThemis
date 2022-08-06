from os import path
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

def read_result(osd: str, sub: classes.Submission) -> None:
    fname = sub.get_file_name(sub)
    
