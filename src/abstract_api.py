from abc import ABC, abstractmethod

class API(ABC):
    """
    абстрактный класс
    """
    @abstractmethod
    def get_vacancies(self, search_query):
        pass