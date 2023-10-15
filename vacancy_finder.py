from api.hh_api import HeadHunterAPI
from api.sj_api import SuperJobAPI
from data_storage.csv_saver import CSVSaver
from data_storage.json_saver import JSONSaver
from data_storage.txt_saver import TxtSaver

json_saver = JSONSaver()
csv_saver = CSVSaver()
txt_saver = TxtSaver()


class VacancyFinder:
    def __init__(self):
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
        while True:
            user_input = input(msg)
            if user_input.isdigit():
                return int(user_input)

    def input_area(self):
        while True:
            self.user_input_area = input("введите населенный пункт: ").capitalize()
            if (t := HeadHunterAPI.area_id_search(self.user_input_area)) is None:
                print('!=hh', t)
                continue
            elif (t := SuperJobAPI.area_id_search(self.user_input_area)) is None:
                print('!=sj', t)
                continue
            else:
                break
            print('Введите город повторно/возможно API его не находит')
        # while True: self.user_input_area = input("Введите населенный пункт: ").capitalize() if
        # self.hh.area_id_search(self.user_input_area) is not None and self.sj.area_id_search(
        # self.user_input_area) is not None:
        #
        #         break
        #     print('Введите город повторно/возможно API его не находит')

    def input_text(self):
        while True:
            self.user_input_text = input("Введите ваш запрос: ").strip()
            if self.user_input_text.isalpha():
                break

    def input_pages_and_salary(self):
        msg = 'Введите количество страниц: '
        self.user_input_pages = self.valid_int(msg)
        msg = "Введите предпочтения по з/п: "
        self.user_input_salary = self.valid_int(msg)

    def collect_params(self):
        self.params = {
            "area": self.user_input_area,
            "text": self.user_input_text,
            "pages": self.user_input_pages,
            "salary": self.user_input_salary
        }

    def get_vacancies(self):
        for api in self.api_list:
            try:
                raw_vacancy = api.get_vacancies(self.params)
                self.vacancy_list.extend(raw_vacancy)
            except ConnectionError:
                print('!=200')
                continue

    def run(self):
        self.input_area()
        self.input_text()
        self.input_pages_and_salary()
        self.collect_params()
        self.get_vacancies()
        if not self.vacancy_list:
            print("No vacancies found.")
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



# from api.hh_api import HeadHunterAPI

# from api.sj_api import SuperJobAPI
# from data_storage.abc_saver import save_json, save_csv, save_txt
#
#
# def valid_int(msg):
#     while True:
#         user_input = input(msg)
#         if user_input.isdigit():
#             return int(user_input)
#
#
# # user_input_area = "Москва"  # input("введите населенный пункт: ").capitalize()
#
# while True:
#     user_input_area = input("введите населенный пункт: ").capitalize()
#     if (t := HeadHunterAPI.area_id_search(user_input_area)) == None:
#         print('!=hh', t)
#         continue
#     elif (t := SuperJobAPI.area_id_search(user_input_area)) == None:
#         print('!=sj', t)
#         continue
#     else:
#         break
#     print('Введите город повторно/возможно API его не находит')
#
# while True:
#     # user_input_text = "Python"  # input("введите ваш запрос: ").strip()
#     user_input_text = input("введите ваш запрос: ").strip()
#     if user_input_text.isalpha():
#         break
#
# msg = 'Введите количество страниц'
# user_input_pages = valid_int(msg)
#
# msg = "Введите предпочтения по з/п"
# user_input_salary = valid_int(msg)
#
# params = {
#     "area": user_input_area,
#     "text": user_input_text,
#     "pages": user_input_pages,
#     "salary": user_input_salary
# }
#
# hh = HeadHunterAPI()
# sj = SuperJobAPI()
# api_list = [hh, sj]
#
# vacancy_list = []
# for api in api_list:
#     try:
#         raw_vacancy = api.get_vacancies(params)
#         # vacancy_list.extend(j for i in raw_vacancy for j in i)
#         vacancy_list.extend(raw_vacancy)
#     except ConnectionError:
#         print('!=200')
#         continue
#
# print(*sorted(vacancy_list), sep='\n')
# while True:
#     user_vacancy_storage = input("сохранить вакнсии в отдельный файл? 1 - да, 2 -нет ")
#     if user_vacancy_storage == "1":
#         storage_extention = input('1 - json | 2 - csv | 3 - txt')
#         if storage_extention == "1":
#             filename = input('Введите имя для JSON файла')
#             save_json(vacancy_list, "data_storage/data/" + filename + ".json")
#         elif storage_extention == "2":
#             filename = input('Введите имя для CSV файла')
#             save_csv(vacancy_list, "data_storage/data/" + filename + ".csv")
#         elif storage_extention == "3":
#             filename = input('Введите имя для TXT файла')
#             save_txt(vacancy_list, "data_storage/data/" + filename + ".txt")
#         else:
#             print("Не верный ввод, повторите попытку")
#             continue
#     elif user_vacancy_storage == "2":
#         print("Благодарим за пользование программой")
#         break
