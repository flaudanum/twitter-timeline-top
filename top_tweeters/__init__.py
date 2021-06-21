from argparse import ArgumentParser

from top_tweeters import errors
from top_tweeters.loader.local_file_loader import LocalFileLoader
from top_tweeters.output import pretty_output
from top_tweeters.ranker import Ranker

# Right now this script only retrieves data from JSON files in the locql file system but in the future this data should
# be requested from the Tweeter API. This hardcoded parameter would then be set from a CLI argument --source.
data_source = 'file system'


def main():
    """
    This function is the application's entry point. It is called w/* arguments when the application is packaged as a
    script with setuptools.
    """
    arg_parser = ArgumentParser(
        description='This application identifies the top users from a Tweeter timeline.'
    )

    arg_parser.add_argument('--top', default=5)
    arg_parser.add_argument('--file')

    args = arg_parser.parse_args()
    try:
        # Number of top users
        top_size: int = int(args.top)

        if data_source == 'file system':
            if not errors.check_input_file(args.file):
                exit(1)

            file_loader = LocalFileLoader(json_file_path=args.file)
            ranker = Ranker(loader=file_loader)
            pretty_output(ranker.top(top_size))

        else:
            raise NotImplementedError('This script only loads data from the local file system')

    except errors.APP_EXCEPTIONS as err:
        if errors.process(err, args):
            exit(1)

        # The exception was not managed
        raise err
