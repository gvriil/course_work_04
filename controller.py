from api.hh_api import HeadHunterAPI
from api.sj_api import SuperJobAPI
from data_storage.json_saver import save_json
from api.hh_api import HeadHunterAPI


class VacancyController:
    def __init__(self, hh_api, sj_api, storage):
        self.hh_api = hh_api
        self.sj_api = sj_api
        self.storage = storage

    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    def get_vacancies(self, search_query):
        hh_vacancies = self.hh.get_vacancies(search_query)
        sj_vacancies = self.sj.get_vacancies(search_query)
        hh_area = self.hh.get_vacancies(search_query['area'])
        hh_json = self.hh.get_vacancies(search_query)
        return self.hh.data_format(hh_json)

        # Обработка данных, сравнение, фильтрация и т. д.

    def save_vacancy(self, vacancy):
        self.storage.add_vacancy(vacancy)

    def get_vacancies_from_storage(self, criteria):
        return self.storage.get_vacancies(criteria)

    def delete_vacancy(self, vacancy):
        self.storage.delete_vacancy(vacancy)
