import json

from data_storage.abc_saver import Saver
from models.vacancy import Vacancy


class JSONSaver(Saver):
    """
    Реализация сейвера для сохранения вакансий в формате JSON.

    Этот класс наследуется от абстрактного класса Saver и предоставляет конкретную реализацию метода save,
    который позволяет сохранить вакансии в JSON файле.

    Attributes:
        None

    Methods:
        save(vacancies: list[Vacancy], filename: str) -> None: Сохраняет список вакансий в файл формата JSON.

    Example:
    ```python
    saver = JSONSaver()
    vacancies = [Vacancy(...), Vacancy(...), ...]
    filename = "vacancies.json"
    saver.save(vacancies, filename)
    ```
    """

    def save(self, vacancies: list[Vacancy], filename: str) -> None:
        """
        Сохраняет список вакансий в файл формата JSON.

        Args:
            vacancies (list[Vacancy]): Список объектов Vacancy, представляющих вакансии для сохранения.
            filename (str): Имя файла, в который нужно сохранить вакансии.

        Returns:
            None

        Example:
        ```python
        saver = JSONSaver()
        vacancies = [Vacancy(...), Vacancy(...), ...]
        filename = "vacancies.json"
        saver.save(vacancies, filename)
        ```
        """
        with open(filename, 'w') as file:
            json.dump([vacancy.get_dict() for vacancy in vacancies],
                      file, ensure_ascii=False, indent=4)
