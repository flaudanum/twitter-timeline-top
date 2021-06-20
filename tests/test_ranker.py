import pandas as pd

from loader.loader import Loader
from timeline_parser import Ranker


class FakeLoader(Loader):
    @property
    def json_data(self):
        return None

    def __init__(self):
        data = {
            'user_id': [100, 101, 102, 200, 201, 202, 100, 101, 102, 100, 101, 101],
            'created_at': ['Fri Sep 16 08:48:17 +0000 2016' for _ in range(12)]
        }
        self._timeline_df = pd.DataFrame.from_dict(data, orient='columns')

        self._user_names = {
            100: 'Max Planck',
            101: 'Grace Hopper',
            102: 'Emmy Noether',
            200: 'User #4',
            201: 'User #5',
            202: 'User #6',
        }

    def __call__(self) -> dict:
        return {
            'data': self._timeline_df,
            'user_names': self._user_names
        }


def test_ranker():
    file_loader = FakeLoader()
    ranker = Ranker(loader=file_loader)

    ref_result = pd.DataFrame.from_dict(
        {
            101: [4, 'Grace Hopper'],
            100: [3, 'Max Planck'],
            102: [2, 'Emmy Noether']
        }
        , orient='index',
        columns=['count', 'names'],
    )
    ref_result.index = ref_result.index.set_names('user_id')

    pd.testing.assert_frame_equal(ranker.top(size=3), ref_result)
