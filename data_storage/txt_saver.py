from data_storage.abc_saver import Saver
from models.vacancy import Vacancy


class TxtSaver(Saver):
    """
    Реализация сейвера для сохранения вакансий в текстовом формате (TXT).

    Этот класс наследуется от абстрактного класса Saver и предоставляет конкретную реализацию метода save,
    который позволяет сохранить вакансии в текстовом файле.

    Attributes:
        None

    Methods:
        save(vacancies: list[Vacancy], filename: str) -> None: Сохраняет список вакансий в текстовом файле.

    Example:
    ```python
    saver = TxtSaver()
    vacancies = [Vacancy(...), Vacancy(...), ...]
    filename = "vacancies.txt"
    saver.save(vacancies, filename)
    ```
    """

    def save(self, vacancies: list[Vacancy], filename: str) -> None:
        """
        Сохраняет список вакансий в текстовом файле.

        Args:
            vacancies (list[Vacancy]): Список объектов Vacancy, представляющих вакансии для сохранения.
            filename (str): Имя файла, в который нужно сохранить вакансии.

        Returns:
            None

        Example:
        ```python
        saver = TxtSaver()
        vacancies = [Vacancy(...), Vacancy(...), ...]
        filename = "vacancies.txt"
        saver.save(vacancies, filename)
        ```
        """
        with open(filename, 'w') as txt_file:
            for vacancy in vacancies:
                txt_file.write(str(vacancy) + '\n')
