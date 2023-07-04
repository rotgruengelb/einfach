import sys, os


def clip(content: str, no_os_error: bool = False):
    if content.isspace() == False and not content == "":
        if sys.platform == "win32":
            try:
                os.system(f'echo {content} | clip')
            except Exception as e: raise e
        elif no_os_error == False:
            raise OSError("Currently only win32 systems are supported!")
    else:
        raise ValueError("Content can't be empty or only contain whitespace/spaces.")