import csv
import json

from models.vacancy import Vacancy


# from storage import DataStorage
def save_json(vacancies: list[Vacancy], filename):
    with open(filename, 'w') as file:
        json.dump([vacancy.get_dict() for vacancy in vacancies], file, ensure_ascii=False,
                  indent=4)


def save_csv(vacancies: list[Vacancy], filename):
    with open(filename, "w", newline="") as f:
        wr = csv.writer(f, delimiter=";")
        wr.writerow(['заголовок', 'описание', 'ссылка', 'з/п', 'город'])
        for vacancy in vacancies:
            wr.writerow(vacancy.to_list())


def save_txt(vacancies: list[Vacancy], filename):
    with open(filename, 'w') as txt_file:
        for vacancy in vacancies:
            txt_file.write(str(vacancy) + '\n')
