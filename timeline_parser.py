from functools import cache

import pandas as pd

from loader.loader import Loader


class Ranker:

    def __init__(self, loader: Loader):
        self._loader = loader

    @cache
    def top(self, size: int):
        res = self._loader()
        data: pd.DataFrame = res['data'].drop(['created_at'], axis=1)
        data['count'] = 1
        user_names = res['user_names']

        ranking = data.groupby('user_id').count()
        ranking['names'] = [user_names[user_id] for user_id in ranking.index]
        ranking = ranking.sort_values(by=['count'], ascending=False)

        return ranking.iloc[:size, :]
