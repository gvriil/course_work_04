from api.hh_api import HeadHunterAPI
from api.sj_api import SuperJobAPI
from models.vacancy import Vacancy

user_input_area = "Москва"  # input("введите населенный пункт: ").capitalize()
user_input_text = "Python"  # input("введите ваш запрос: ").strip()
user_input_platform = input('''Выберите платформу
1 - HeadHunter
2 - SuperJob
3 - HeadHunter + SuperJob
''')

params = {
    "area": user_input_area,
    "text": user_input_text,
}

api_list = []

if user_input_platform in ["1", "3"]:
    hh = HeadHunterAPI()
    hh_area = hh.area_id_search(user_input_area)
    hh_json = hh.get_vacancies(params)
    api_list.extend(hh.data_format(hh_json))

if user_input_platform in ["2", "3"]:
    sj = SuperJobAPI()
    sj_area = sj.area_id_search(user_input_area)
    sj_json = sj.get_vacancies(params)
    api_list.extend(sj.data_format(sj_json))

vacancy_list = [Vacancy(*data) for data in api_list]

print('Отсортировать по ЗП')
print(*sorted(vacancy_list), sep='\n')
