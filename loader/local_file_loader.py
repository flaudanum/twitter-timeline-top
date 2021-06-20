import json
from pathlib import Path

import pandas as pd

from loader.loader import Loader


def local_file_loader(json_file_path):
    file_path = Path(json_file_path)

    with file_path.open('r') as text_out:
        return json.load(text_out)


class LocalFileLoader(Loader):

    @property
    def json_data(self):
        return self._json_data

    def __init__(self, json_file_path, file_reader=local_file_loader):
        self._json_data = file_reader(json_file_path)

    def __call__(self) -> dict:
        data = {
            'user_id': [],
            'created_at': []
        }
        user_names = {}

        for raw_tweet in self._json_data:
            user_id = raw_tweet['user']['id']
            data['user_id'].append(user_id)
            data['created_at'].append(raw_tweet['created_at'])

            user_names[user_id] = raw_tweet['user']['name']

        return {
            'data': pd.DataFrame.from_dict(data, orient='columns'),
            'user_names': user_names
        }
