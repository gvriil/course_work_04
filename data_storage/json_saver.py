import json
from abc import ABC

from storage import DataStorage


def save_json(vacancies, filename):
    pass

    with open(filename, 'w') as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=4)


class DataJson(DataStorage, ABC):
    def __init__(self, filename, vacancies):
        self.file_name = filename
        self.vacancies = vacancies
