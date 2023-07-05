import tkinter as tk
from tkinter import filedialog
from einfach import errors as errors


def open_file(mode, **filedialogargs):
    root = tk.Tk()
    root.withdraw()
    try:
        if mode == "file":
            file_path = filedialog.askopenfile(**filedialogargs)
            return file_path
        if mode == "file_name":
            file_path = filedialog.askopenfilename(**filedialogargs)
            return file_path
        if mode == "files":
            file_path = filedialog.askopenfiles(**filedialogargs)
            return file_path
        if mode == "file_names":
            file_path = filedialog.askopenfilenames(**filedialogargs)
            return file_path
        raise ValueError(errors.FILE_DIALOG_INVALID_MODE)
    except Exception as exception:
        raise exception


def save_file(mode, **filedialogargs):
    root = tk.Tk()
    root.withdraw()
    try:
        if mode == "file":
            file_path = filedialog.asksaveasfile(**filedialogargs)
            return file_path
        if mode == "file_name":
            file_path = filedialog.asksaveasfilename(**filedialogargs)
            return file_path
        if mode == "files":
            file_path = filedialog.askopenfiles(**filedialogargs)
            return file_path
        if mode == "file_names":
            file_path = filedialog.askopenfilenames(**filedialogargs)
            return file_path
        raise ValueError(errors.FILE_DIALOG_INVALID_MODE)
    except Exception as exception:
        raise exception


def open_dir(**dirdialogargs):
    root = tk.Tk()
    root.withdraw()
    try:
        dir_path = filedialog.askdirectory(**dirdialogargs)
        return dir_path
    except Exception as exception:
        raise exception
