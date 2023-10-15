import requests
from api.abc_api import VacancyAPI
from config import PER_PAGE
from models.currency import Currency
from models.vacancy import Vacancy

class HeadHunterAPI(VacancyAPI):
    """
    Класс для взаимодействия с API HeadHunter для получения вакансий.
    """

    cache = {}
    per_page = PER_PAGE

    def get_vacancies(self, search_query: dict):
        """
        Получение вакансий с помощью API HeadHunter на основе параметров поиска.

        Args:
            search_query (dict): Словарь, содержащий параметры поиска.

        Returns:
            list[Vacancy]: Список объектов Vacancy, представляющих вакансии.
        """

        url = "https://api.hh.ru/vacancies"
        pages_amount = search_query["pages"]
        params = {
            "text": search_query["text"],
            "area": self.area_id_search(search_query["area"]),
            "per_page": self.per_page,
            "salary": search_query["salary"],
            "no_agreement": 1
        }
        res = []

        for page in range(pages_amount):
            params['page'] = page
            response = requests.get(url, params=params)

            if response.status_code != 200:
                raise ConnectionError('Ошибка связи с API')

            result = HeadHunterAPI._data_format(response.json())
            if result:
                res.extend(result)

        return res

    @staticmethod
    def _data_format(data) -> list[Vacancy]:
        """
        Форматирование необработанных данных из ответа API в список объектов Vacancy.

        Args:
            data: Необработанные данные из ответа API.

        Returns:
            list[Vacancy]: Список объектов Vacancy.
        """

        vacancies = []
        for item in data['items']:
            title = item['name']
            link = item['alternate_url']
            salary = item['salary']

            if salary:
                salary_from = salary.get('from', None)
                cur = salary.get("currency", None)
                salary_to = salary.get('to', None)

                if salary_from and salary_to:
                    salary = (salary_from + salary_to) / 2
                else:
                    salary = salary_from if salary_from else salary_to

                salary = Currency(salary, cur)
            else:
                continue
                # salary = Currency(0, ':)')

            description = item['snippet']['responsibility']
            town = item['area']['name']
            vacancy = Vacancy(title, link, salary, description, town)

            vacancies.append(vacancy)

        return vacancies

    @classmethod
    def area_id_search(cls, city):
        """
        Проверка правильности введенного названия города и получение его ID из API.

        Args:
            city (str): Название города.

        Returns:
            int | None: ID города или None, если не найден.
        """

        url = 'https://api.hh.ru/areas'
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception('HeadHunterAPI: Ошибка запроса городов, API не работает')

        response_json = response.json()

        return cls.find_area(city, response_json)

    @classmethod
    def find_area(cls, city_title: str, areas: dict) -> int | None:
        """
        Рекурсивный поиск ID города по его названию в словаре районов.

        Args:
            city_title (str): Название города для поиска.
            areas (dict): Словарь районов с определенной структурой.

        Returns:
            int | None: ID города или None, если не найден.
        """

        for area in areas:
            if area['name'] == city_title:
                return area['id']
            elif area['areas']:
                result = cls.find_area(city_title, area['areas'])
                if result:
                    return int(result)
