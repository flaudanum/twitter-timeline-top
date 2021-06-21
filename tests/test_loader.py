import pandas as pd
import pytest


from tests import tweets_fixture
from top_tweeters import LocalFileLoader


def fake_file_loader(json_file_path: str):
    if json_file_path != './dummy/path/to/file':
        raise ValueError(json_file_path)

    return tweets_fixture.tweets()


@pytest.fixture(scope='function', name='loader')
def loader_fixture():
    return LocalFileLoader(
        json_file_path='./dummy/path/to/file',
        file_reader=fake_file_loader
    )


def test_local_file_loader_should_load_json_data(loader):
    # 4 elements loaded
    assert len(loader.json_data) == 4

    for tweet in loader.json_data:
        assert {'created_at', 'user'} <= set(tweet)
        assert {'id', 'name'} <= set(tweet['user'])


def test_local_file_loader_should_provide_filtered_data(loader):
    res = loader()

    filtered_data = res['data']
    user_names = res['user_names']

    assert isinstance(filtered_data, pd.DataFrame)

    assert filtered_data.shape == (4, 2)

    assert list(filtered_data.columns) == ['user_id', 'created_at']

    assert user_names == {
        183749519: 'Paul Graham',
        592843104: 'François GEUZE',
        30183861: 'Matthieu Lux',
        1269648812: 'Le Lab RH'
    }
