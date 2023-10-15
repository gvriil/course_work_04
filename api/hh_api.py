import requests

from api.abc_api import VacancyAPI
from models.currency import Currency
from models.vacancy import Vacancy


class HeadHunterAPI(VacancyAPI):
    cache = {}

    def get_vacancies(self, search_query: dict):
        # cache_hash = str(search_query)
        # if cache_hash in self.cache:
        #     return self.cache[cache_hash]
        url = "https://api.hh.ru/vacancies"

        pages_amount = search_query["pages"]
        params = {
            "text": search_query["text"],
            "area": self.area_id_search(search_query["area"]),
            "per_page": 10,
            "salary": search_query["salary"],
            "no_agreement": 1
        }

        res = []
        for page in range(pages_amount):
            params['page'] = page

            response = requests.get(url, params=params)

            if response.status_code != 200:
                raise ConnectionError('Ошибка связи с API')

            # raw_vacancy.append(response)

            result = HeadHunterAPI._data_format(response.json())
            if result:
                res.extend(result)

        return res

    @staticmethod
    def _data_format(data) -> list[Vacancy]:

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
                salary = Currency(0, ':)')
            description = item['snippet']['responsibility']
            town = item['area']['name']
            vacancy = Vacancy(title, link, salary, description, town)

            vacancies.append(vacancy)
        return vacancies

    @classmethod
    def area_id_search(cls, city):
        """ Метод для проверки введенного города """

        url = 'https://api.hh.ru/areas'
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception('HeadHunterAPI: Ошибка запроса городов, api не работает')

        response_json = response.json()

        return cls.find_area(city, response_json)

    @classmethod
    def find_area(cls, city_title: str, areas: dict) -> int | None:
        """
        Рекурсивный метод для поиска города по названию
        :param city_title: название города
        :param areas: словарик с городами и определенной структурой смотреть
        (https://github.com/hhru/api/blob/master/docs/areas.md#areas)
        :return: id города или None
        """

        for area in areas:
            if area['name'] == city_title:
                return area['id']
            elif area['areas']:
                result = cls.find_area(city_title, area['areas'])
                if result:
                    return int(result)
