import json
from abc import ABC

from models.vacancy import Vacancy
# from storage import DataStorage


def save_json(vacancies: list[Vacancy], filename):

    with open(filename, 'w') as file:
        json.dump([vacancy.get_dict() for vacancy in vacancies], file, ensure_ascii=False, indent=4)


# class DataJson(DataStorage, ABC):
#     def __init__(self, filename, vacancies):
#         self.file_name = filename
#         self.vacancies = vacancies
