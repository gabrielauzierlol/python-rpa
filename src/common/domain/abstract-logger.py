from abc import ABC, abstractmethod


class AbstractLogger(ABC):

    @abstractmethod
    def debug(self, message: str, extra: object):
        pass

    @abstractmethod
    def info(self, message: str, extra: object):
        pass

    @abstractmethod
    def warn(self, message: str, extra: object):
        pass

    @abstractmethod
    def error(self, message: str, extra: object):
        pass
