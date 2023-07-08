import sys
import os
from einfach import errors


def copy(content: str, no_os_error: bool = False):
    if content.isspace() is False and not content == "":
        try:
            if sys.platform == 'win32':
                os.system(f'echo {content} | clip')
            if sys.platform == 'darwin':
                os.system(f'printf {content} | pbcopy')
            elif no_os_error is False:
                raise OSError(errors.CLIP_COMPAT)
        except Exception as exception:
            raise exception
    else:
        raise ValueError(errors.WHITE_BLANK_SPACE_ERR)
