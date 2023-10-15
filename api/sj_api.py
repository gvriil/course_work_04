import os

import requests

from api.abc_api import VacancyAPI
from models.currency import Currency
from models.vacancy import Vacancy


class SuperJobAPI(VacancyAPI):
    # api_url = 'https://api.superjob.ru/2.0/vacancies'3
    api_key = os.getenv('API_KEY_SJ')
    headers = {"X-Api-App-Id": api_key}
    cache = {}
    def get_vacancies(self, search_query):
        cache_hash = str(search_query)
        if cache_hash in self.cache:
            return self.cache[cache_hash]
        url = 'https://api.superjob.ru/2.0/vacancies/'

        # self.area = search_query["town"]
        pages_amount = search_query["pages"]

        params = {
            "keyword": search_query.get('text'),
            "town": self.area_id_search(search_query["area"]),
            "count": 10,
            "payment_from": search_query["salary"],
            "only_with_salary": True
        }

        res = []
        for page in range(pages_amount):
            params['page'] = page

            response = requests.get(url, params=params, headers=self.headers)

            if response.status_code != 200:
                raise ConnectionError('Ошибка связи с API')

            result = SuperJobAPI._data_format(response.json())
            if result:
                res.extend(result)

        return res

    @staticmethod
    def _data_format(data):
        vacancies = []

        if 'objects' in data:
            vacancy_data = data['objects']
            for item in vacancy_data:
                title = item.get('profession', 'N/A')
                link = item.get('link', 'N/A')

                # payment_from = item.get('payment_from', None)
                # payment_to = item.get('payment_to', None)

                salary_from = item.get('payment_from', None)
                cur = item.get("currency", None)
                salary_to = item.get('payment_to', None)
                if salary_from and salary_to:
                    salary = (salary_from + salary_to) / 2
                else:
                    salary = salary_from if salary_from else salary_to
                salary = Currency(salary, cur)

                description = item.get('work', 'N/A')
                town = item.get('town', {}).get('title', 'N/A')
                vacancy = Vacancy(title, link, salary, description, town)

                vacancies.append(vacancy)

            return vacancies

    @classmethod
    def area_id_search(cls, city_title):
        """ Метод для проверки введенного города """
        params = {'all': True}

        url = 'https://api.superjob.ru/2.0/towns/'
        response = requests.get(url, headers=cls.headers, params=params)

        if response.status_code != 200:
            raise Exception('SuperJobAPI: Ошибка запроса городов, api не работает')

        response_json = response.json()['objects']
        for city in response_json:
            if city['title'] == city_title:
                return city['id']
