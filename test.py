from unittest.mock import Mock, patch
import sys
import pytest
from einfach import termutils, clip, floatutils, pathdialog, __license__, __version__
from einfach.internal import errors


print(__version__, __license__)

def test_clip_success():
    platform = sys.platform
    sys.platform = "win32"
    content = "Hello, world!"
    clip.clip(content)
    # Assert that the content is successfully clipped to the clipboard
    # You can add additional assertions here to check the clipboard contents
    assert True
    sys.platform = platform


def test_clip_with_no_os_error():
    platform = sys.platform
    sys.platform = "win32"
    content = "Hello, world!"
    clip.clip(content, no_os_error = True)
    # Assert that the content is successfully clipped to the clipboard
    # You can add additional assertions here to check the clipboard contents
    assert True
    sys.platform = platform


def test_clip_empty_content():
    platform = sys.platform
    sys.platform = "win32"
    with pytest.raises(ValueError) as excinfo:
        content = ""
        clip.clip(content)
    # Assert that a ValueError is raised with the appropriate message
    assert str(excinfo.value) == f"{errors.FILE_DIALOG_INVALID_MODE}"
    sys.platform = platform


def test_clip_whitespace_content():
    platform = sys.platform
    with pytest.raises(ValueError) as excinfo:
        sys.platform = "win32"
        content = "   "
        clip.clip(content)
    # Assert that a ValueError is raised with the appropriate message
    assert str(excinfo.value) == f"{errors.FILE_DIALOG_INVALID_MODE}"
    sys.platform = platform


def test_clip_non_supported_platform():
    platform = sys.platform
    with pytest.raises(OSError) as excinfo:
        content = "Hello, world!"
        sys.platform = "linux"  # Simulating a non-supported platform
        clip.clip(content)
    # Assert that an OSError is raised with the appropriate message
    assert str(excinfo.value) == f"{errors.ONLY_WIN32}"
    sys.platform = platform  # Restore the original platform value



def test_would_be_valid_float_valid_input():
    value = "3.14"
    assert floatutils.would_be_valid_float(value) is True


def test_would_be_valid_float_invalid_input():
    value = "not a float"
    assert floatutils.would_be_valid_float(value) is False


def test_is_float_in_range_within_range():
    value = 5.0
    min_value = 1.0
    max_value = 10.0
    assert floatutils.is_float_in_range(value, min_value, max_value) is True


def test_is_float_in_range_below_range():
    value = 0.5
    min_value = 1.0
    max_value = 10.0
    assert floatutils.is_float_in_range(value, min_value, max_value) is False


def test_is_float_in_range_above_range():
    value = 15.0
    min_value = 1.0
    max_value = 10.0
    assert floatutils.is_float_in_range(value, min_value, max_value) is False


def test_is_float_in_range_at_boundary():
    value = 10.0
    min_value = 1.0
    max_value = 10.0
    assert floatutils.is_float_in_range(value, min_value, max_value) is True


def test_is_float_in_range_with_integer_values():
    value = 5
    min_value = 1
    max_value = 10
    assert floatutils.is_float_in_range(value, min_value, max_value) is True



@pytest.mark.parametrize("mode", ["file", "file_name", "files", "file_names"])
def test_open_file_valid_modes(mode):
    with patch("einfach.pathdialog.tk.Tk"):
        filedialog_mock = Mock()
        filedialog_mock.askopenfile.return_value = "file_path"
        filedialog_mock.askopenfilename.return_value = "file_path"
        filedialog_mock.askopenfiles.return_value = ["file_path"]
        filedialog_mock.askopenfilenames.return_value = ["file_path"]
        with patch("einfach.pathdialog.filedialog", filedialog_mock):
            file_path = pathdialog.open_file(mode)
            if isinstance(file_path, list):
                file_path = file_path[0]
            assert file_path == "file_path"


def test_open_file_invalid_mode():
    with patch("einfach.pathdialog.tk.Tk"):
        with pytest.raises(ValueError) as excinfo:
            mode = "invalid_mode"
            pathdialog.open_file(mode)
        assert str(excinfo.value) == f"{errors.FILE_DIALOG_INVALID_MODE}"


@pytest.mark.parametrize("mode", ["file", "file_name", "files", "file_names"])
def test_save_file_valid_modes(mode):
    with patch("einfach.pathdialog.tk.Tk"):
        filedialog_mock = Mock()
        filedialog_mock.asksaveasfile.return_value = "file_path"
        filedialog_mock.asksaveasfilename.return_value = "file_path"
        filedialog_mock.askopenfiles.return_value = ["file_path"]
        filedialog_mock.askopenfilenames.return_value = ["file_path"]
        with patch("einfach.pathdialog.filedialog", filedialog_mock):
            file_path = pathdialog.save_file(mode)
            if isinstance(file_path, list):
                file_path = file_path[0]
            assert file_path == "file_path"


def test_save_file_invalid_mode():
    with patch("einfach.pathdialog.tk.Tk"):
        with pytest.raises(ValueError) as excinfo:
            mode = "invalid_mode"
            pathdialog.save_file(mode)
        assert str(excinfo.value) == "mode was not 'file', 'file_name', 'files' or 'file_names'!"


def test_open_dir():
    with patch("einfach.pathdialog.tk.Tk"):
        filedialog_mock = Mock()
        filedialog_mock.askdirectory.return_value = "dir_path"
        with patch("einfach.pathdialog.filedialog", filedialog_mock):
            dir_path = pathdialog.open_dir()
            assert dir_path == "dir_path"


# @pytest.mark.timeout(5)
# def test_async_user_input_calls_input_function_and_callback():
#     input_values = ["test_input"]  # Predefined input values for testing
#     callback_mock = Mock()

#     with patch("einfach.termutils.input", side_effect = input_values):
#         async_user_input=termutils.AsyncUserInput(callback_mock, input_function=input)
#         async_user_input.pause()
#         async_user_input.resume()
#         async_user_input.join()

#     assert callback_mock.call_count == len(input_values)
#     for value in input_values:
#         callback_mock.assert_called_with(value)


# def test_async_user_input_pauses_and_resumes():
#     input_mock = Mock()
#     callback_mock = Mock()
#     async_input = termutils.AsyncUserInput(input_callback=callback_mock, input_function=input_mock)


#     async_input.pause()
#     assert async_input.paused


#     input_mock.assert_not_called()
#     callback_mock.assert_not_called()


#     async_input.resume()
#     async_input.join()


#     input_mock.assert_called_once()
#     callback_mock.assert_called_once()



def test_async_user_input_thread_name():
    callback_mock = Mock()
    async_input = termutils.AsyncUserInput(input_callback=callback_mock)

    assert async_input.name == 'AsyncUserInput-thread'


def test_async_user_input_invokes_callback_multiple_times():
    input_mock = Mock(side_effect = ["input_1", "input_2", "input_3", "input_4", "input_5"])
    callback_mock = Mock()
    async_input = termutils.AsyncUserInput(input_callback = callback_mock, input_function = input_mock)
    async_input.join()
    input_mock.assert_called_with()
    assert callback_mock.call_count == 5


@pytest.fixture
def async_input_thread():
    input_mock = Mock(return_value="user_input")
    callback_mock = Mock()
    async_input = termutils.AsyncUserInput(input_callback = callback_mock, input_function = input_mock)
    yield async_input
    async_input.pause()
    async_input.resume()
    async_input.join()


# def test_async_user_input_fixture_calls_input_function_and_callback(async_input_thread):
#     input_mock = async_input_thread.input_function
#     callback_mock = async_input_thread.input_callback
#     assert input_mock.call_count == 1
#     assert callback_mock.call_count == 1
#     assert callback_mock.call_args == (("user_input",),)


# def test_async_user_input_fixture_pauses_and_resumes(async_input_thread):
#     async_input_thread.pause()
#     assert async_input_thread.paused
#     async_input_thread.input_function.assert_not_called()
#     async_input_thread.input_callback.assert_not_called()
#     async_input_thread.resume()
#     async_input_thread.join()
#     async_input_thread.input_function.assert_called_once()
#     async_input_thread.input_callback.assert_called_once()

