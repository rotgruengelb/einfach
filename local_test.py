# # from einfach import clip, pathdialog, filetools

# # try:
# #     clip.clip(content="mia", no_os_error=True)
# # except Exception as E:
# #     print(E)


# # print(pathdialog.open_file(mode="file_name"))

# # print(pathdialog.save_file(mode="files", title="abba", initialdir="C:/Documents"))

# # print(pathdialog.open_dir())


# # clip.clip(content="Hello World") # this wont ignore the OSError when not run on win32
# # clip.clip(content="Hi! :D", no_os_error=True) # this will ignore the OSError if run on a non win32 platform. This will result in the clipboard not changing on the non-win32 os. 


# # valid_args = [("name", "n", 2), ("type", "t", 1)]

# # args = sysargs.arg_handler(valid_args)
# # print(args)



# # file = pathdialog.open_file(mode="file_name")

# # hashes = [filetools.SHAHash.sha1(text_or_file=file),filetools.SHAHash.sha224(text_or_file=file),filetools.SHAHash.sha256(text_or_file=file),filetools.SHAHash.sha384(text_or_file=file),filetools.SHAHash.sha512(text_or_file=file)]

# # print(filetools.SHAHash.check_hash(file, hashes))

# def test_func():
#     return None

# def test(func):
#     return type(func)

# print(test(test_func))

from einfach import termutils, __version__
from time import sleep

print(__version__)

def callback(input):
    for x in range(10):
        print(f"Got: {input}")


AUI = termutils.AsyncUserInput(
    input_callback=callback,
)

while True:
    sleep(1)
    print(".")