from abc import ABC, abstractmethod

from models.vacancy import Vacancy


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search_query)-> list[Vacancy]:
        pass

