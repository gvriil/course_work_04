import csv

from data_storage.abc_saver import Saver
from models.vacancy import Vacancy


class CSVSaver(Saver):
    """
    Реализация сейвера для сохранения вакансий в формате CSV.

    Этот класс наследуется от абстрактного класса Saver и предоставляет конкретную реализацию метода save,
    который позволяет сохранить вакансии в CSV файле с заданным разделителем.
    """

    def save(self, vacancies: list[Vacancy], filename):
        """
        Сохраняет список вакансий в файл формата CSV.

        :param vacancies: Список объектов Vacancy, представляющих вакансии для сохранения.
        :type vacancies: list[Vacancy]

        :param filename: Имя файла, в который нужно сохранить вакансии.
        :type filename: str
        """
        with open(filename, "w", newline="") as f:
            wr = csv.writer(f, delimiter=";")
            wr.writerow(['заголовок', 'описание', 'ссылка', 'з/п', 'город'])
            for vacancy in vacancies:
                wr.writerow(vacancy.to_list())
