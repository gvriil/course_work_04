from abc import ABC, abstractmethod

from models.vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def save(self, vacancies: list[Vacancy], filename):
        pass

