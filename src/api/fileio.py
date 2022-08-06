import os
from src.api import classes

class FileIOException(Exception):
    '''Class for throwing exceptions around'''

def write_file(fpath: str, content: str) -> None:
    '''Write a file to a folder. Throws if file already exists.'''
    if os.path.exists(fpath):
        raise FileIOException(f"Duplicated file. Name: {fpath}")
    sanitized_code = content.encode("ascii", errors="ignore")
    with open(fpath, 'xb') as submit_file:
        submit_file.write(sanitized_code)
