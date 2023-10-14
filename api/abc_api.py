from abc import ABC, abstractmethod


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search_query):
        pass

    @abstractmethod
    def data_format(self, data):
        pass
