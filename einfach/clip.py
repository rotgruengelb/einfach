import sys
import os
from internal import errors


def clip(content: str, no_os_error: bool = False):
    if content.isspace() is False and not content == "":
        if sys.platform == "win32":
            try:
                os.system(f'echo {content} | clip')
            except Exception as e:
                raise e
        elif no_os_error is False:
            raise OSError(errors.ONLY_WIN32)
    else:
        raise ValueError(errors.WHITE_BLANK_SPACE_ERR)
