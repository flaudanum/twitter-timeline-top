from pathlib import Path
from sys import stderr
from typing import Optional

APP_EXCEPTIONS = ValueError


def process(err: Exception, script_args):
    """
    Manage exceptions raised within the application by providing an explicit message to the user.

    :param err: the raised exception
    :param script_args: CLI named arguments
    :return: ``True`` if the exception was managed else false
    """
    if 'invalid literal for int()' in err.args[0]:
        stderr.write(f'top-tweeters: argument \'top\' must be an integer: \'{script_args.top}\'\n\n')
        return True

    return False


def check_input_file(file_arg: Optional[str]):
    """
    Checks for a file in the local file system provided as data source
    :return:
    """
    # Error: argument --file was not provided
    if not file_arg:
        stderr.write('The argument --file is required')
        return False

    file_path = Path(file_arg)

    # Error: argument --file is not an existing file path
    if not file_path.is_file():
        stderr.write('The file path provided with argument --file does not exist:\n'
                     f'\'{file_path.absolute()}\'\n\n')
        return False

    return True
