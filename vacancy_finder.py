from api.hh_api import HeadHunterAPI
from api.sj_api import SuperJobAPI
from data_storage.csv_saver import CSVSaver
from data_storage.json_saver import JSONSaver
from data_storage.txt_saver import TxtSaver

# Создаем экземпляры классов для сохранения данных в разных форматах
json_saver = JSONSaver()
csv_saver = CSVSaver()
txt_saver = TxtSaver()

class VacancyFinder:
    def __init__(self):
        """Инициализация класса VacancyFinder.

        Класс предназначен для поиска и сохранения вакансий с разных платформ.
        """
        self.user_input_area = None
        self.user_input_text = None
        self.user_input_pages = None
        self.user_input_salary = None
        self.params = None
        self.hh = HeadHunterAPI()
        self.sj = SuperJobAPI()
        self.api_list = [self.hh, self.sj]
        self.vacancy_list = []

    @staticmethod
    def valid_int(msg):
        """Проверяет, является ли введенная пользователем строка целым числом.

        Args:
            msg (str): Сообщение, запрашивающее ввод пользователя.

        Returns:
            int: Введенное целое число.
        """
        while True:
            user_input = input(msg)
            if user_input.isdigit():
                return int(user_input)

    def input_area(self):
        """Получает населенный пункт от пользователя и проверяет его валидность."""
        while True:
            self.user_input_area = input("Введите населенный пункт: ").capitalize()
            if (t := HeadHunterAPI.area_id_search(self.user_input_area)) is None:
                print('Город не найден на HeadHunter:', self.user_input_area)
                continue
            elif (t := SuperJobAPI.area_id_search(self.user_input_area)) is None:
                print('Город не найден на SuperJob:', self.user_input_area)
                continue
            else:
                break
            print('Введите город повторно/возможно API его не находит')

    def input_text(self):
        """Получает поисковый запрос от пользователя и проверяет его валидность."""
        while True:
            self.user_input_text = input("Введите ваш запрос: ").strip()
            if self.user_input_text.isalpha():
                break

    def input_pages_and_salary(self):
        """Получает количество страниц и предпочтения по зарплате от пользователя."""
        msg = 'Введите количество страниц: '
        self.user_input_pages = self.valid_int(msg)
        msg = "Введите предпочтения по з/п: "
        self.user_input_salary = self.valid_int(msg)

    def collect_params(self):
        """Собирает параметры для поиска вакансий."""
        self.params = {
            "area": self.user_input_area,
            "text": self.user_input_text,
            "pages": self.user_input_pages,
            "salary": self.user_input_salary
        }

    def get_vacancies(self):
        """Получает вакансии с разных платформ и сохраняет их в vacancy_list."""
        for api in self.api_list:
            try:
                raw_vacancy = api.get_vacancies(self.params)
                self.vacancy_list.extend(raw_vacancy)
            except ConnectionError:
                print('Ошибка при получении вакансий')
                continue

    def run(self):
        """Запускает программу для поиска и сохранения вакансий."""
        self.input_area()
        self.input_text()
        self.input_pages_and_salary()
        self.collect_params()
        self.get_vacancies()
        if not self.vacancy_list:
            print("Вакансии не найдены.")
            return

        print(*sorted(self.vacancy_list), sep='\n')

        while True:
            user_vacancy_storage = input("Сохранить вакансии в отдельный файл? 1 - да, 2 - нет: ")
            if user_vacancy_storage == "1":
                storage_extension = input('1 - JSON | 2 - CSV | 3 - TXT: ')
                if storage_extension == "1":
                    filename = input('Введите имя для JSON файла: ')
                    json_saver.save(self.vacancy_list, f"data_storage/data/{filename}.json")
                elif storage_extension == "2":
                    filename = input('Введите имя для CSV файла: ')
                    csv_saver.save(self.vacancy_list, f"data_storage/data/{filename}.csv")
                elif storage_extension == "3":
                    filename = input('Введите имя для TXT файла: ')
                    txt_saver.save(self.vacancy_list, f"data_storage/data/{filename}.txt")
                else:
                    print("Неверный ввод, повторите попытку.")
                    continue
            elif user_vacancy_storage == "2":
                print("Благодарим за пользование программой.")
                break
