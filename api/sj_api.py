import os

import requests

from api.abc_api import VacancyAPI
from models.currency import Currency
from models.vacancy import Vacancy


class SuperJobAPI(VacancyAPI):
    # api_url = 'https://api.superjob.ru/2.0/vacancies'3
    api_key = os.getenv('API_KEY_SJ')
    headers = {"X-Api-App-Id": api_key}

    def get_vacancies(self, search_query):
        url = 'https://api.superjob.ru/2.0/vacancies/'
        # self.area = search_query["town"]

        params = {
            "keyword": search_query.get('text'),
            "town": self.area_id_search(search_query["area"]),
            "count": 10
        }
        response = requests.get(url, params=params, headers=self.headers)
        if response.status_code != 200:
            raise ConnectionError('Ошибка связи с API')
        return SuperJobAPI._data_format(response.json())

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
        #         if payment_from and payment_to:
        #             average_salary = (payment_from + payment_to) // 2
        #             salary_ = f"{average_salary} {item.get('currency', 'N/A')}"
        #         elif payment_from:
        #             salary_ = f"{payment_from} {item.get('currency', 'N/A')}"
        #         elif payment_to != 'N/A':
        #             salary_ = f"До {payment_to} {item.get('currency', 'N/A')}"
        #         else:
        #             salary_ = 'Не указана'
        #
        #         description = item.get('work', 'N/A')
        #         town = item.get('town', {}).get('title', 'N/A')
        #
        #         vacancy = tuple([title, link, salary_, description, town])
        #         vacancies.append(vacancy)
        # return vacancies

    @classmethod
    def area_id_search(cls, city):
        """ Метод для проверки введенного города """

        url = 'https://api.superjob.ru/2.0/towns/'
        response = requests.get(url, headers=SuperJobAPI.headers)

        if response.status_code != 200:
            raise Exception('SuperJobAPI: Ошибка запроса городов, api не работает')

        response_json = response.json()

        return cls.find_area(city, response_json['objects'])

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
            if area['title'] == city_title:
                return area['id']
            elif area['title']:
                result = cls.find_area(city_title, area['title'])
                if result:
                    return int(result)
