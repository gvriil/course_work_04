from models.currency import Currency


class Vacancy:
    def __init__(self, title: str, link: str, salary: Currency, description: str, town: str):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.town = town

    def __repr__(self):
        return f"заголовок: {self.title}\n" \
               f"описание: {self.description}\n" \
               f"ссылка: {self.link}\n" \
               f"з/п: {self.salary}\n" \
               f"город: {self.town}\n"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        if not issubclass(other.__class__, Vacancy):
            raise TypeError('Нельзя сравнить!')
        if self.salary is None:
            return True
        if other.salary is None:
            return False
        # if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float)):
        #     return self.salary < other.salary
        return self.salary < other.salary

    def __le__(self, other):
        if not issubclass(other.__class__, Vacancy.__class__):
            raise TypeError('Нельзя сравнить!')
        if self.salary is None:
            return True
        if other.salary is None:
            return False

        return self.salary <= other.salary

    def get_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "salary": {
                "value": self.salary.value,
                "currency": self.salary.currency
            } if self.salary else None,
            "description": self.description,
            "town": self.town
        }

# from API_Head_Hunter import HeadHunterAPI
# from API_Super_Job import SuperJobAPI
# from vacancy import Vacancy
#
# user_input_area = "Москва"  # input("введите населенный пункт: ").capitalize()
# user_input_text = "Python"  # input("введите ваш запрос: ").strip()
# user_input_platform = input('''Выберите платформу
# 1 - HeadHunter
# 2 - SuperJob
# 3 - HeadHunter + SuperJob
# ''')
#
# params = {
#     "area": user_input_area,
#     "text": user_input_text,
# }
#
# api_list = []
#
# if user_input_platform in ["1", "3"]:
#     hh = HeadHunterAPI()
#     hh_area = hh.area_id_search(user_input_area)
#     hh_json = hh.get_vacancies(params)
#     api_list.extend(hh.data_format(hh_json))
#
# if user_input_platform in ["2", "3"]:
#     sj = SuperJobAPI()
#     sj_area = sj.area_id_search(user_input_area)
#     sj_json = sj.get_vacancies(params)
#     api_list.extend(sj.data_format(sj_json))
#
# vacancy_list = [Vacancy(*data) for data in api_list]
#
# print('Отсортировать по ЗП')
# print(*sorted(vacancy_list), sep='\n')
