from abc import ABC, abstractmethod


class HttpRequest(ABC):
    @abstractmethod
    def get_parameter_values(self, key):
        pass
