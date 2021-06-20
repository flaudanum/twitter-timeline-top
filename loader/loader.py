from abc import ABC, abstractmethod


class Loader(ABC):

    @property
    @abstractmethod
    def json_data(self):
        pass

    @abstractmethod
    def __call__(self) -> dict:
        pass
