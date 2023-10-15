from api.hh_api import HeadHunterAPI
from api.sj_api import SuperJobAPI
from data_storage.saver import save_json, save_csv, save_txt


def valid_int(msg):
    while True:
        user_input = input(msg)
        if user_input.isdigit():
            return int(user_input)


# user_input_area = "Москва"  # input("введите населенный пункт: ").capitalize()

while True:
    user_input_area = input("введите населенный пункт: ").capitalize()
    if (t := HeadHunterAPI.area_id_search(user_input_area)) == None:
        print('!=hh', t)
        continue
    elif (t := SuperJobAPI.area_id_search(user_input_area)) == None:
        print('!=sj', t)
        continue
    else:
        break
    print('Введите город повторно/возможно API его не находит')

while True:
    # user_input_text = "Python"  # input("введите ваш запрос: ").strip()
    user_input_text = input("введите ваш запрос: ").strip()
    if user_input_text.isalpha():
        break

msg = 'Введите количество страниц'
user_input_pages = valid_int(msg)

msg = "Введите предпочтения по з/п"
user_input_salary = valid_int(msg)

params = {
    "area": user_input_area,
    "text": user_input_text,
    "pages": user_input_pages,
    "salary": user_input_salary
}

hh = HeadHunterAPI()
sj = SuperJobAPI()
api_list = [hh, sj]

vacancy_list = []
for api in api_list:
    try:
        raw_vacancy = api.get_vacancies(params)
        # vacancy_list.extend(j for i in raw_vacancy for j in i)
        vacancy_list.extend(raw_vacancy)
    except ConnectionError:
        print('!=200')
        continue

print(*sorted(vacancy_list), sep='\n')
while True:
    user_vacancy_storage = input("сохранить вакнсии в отдельный файл? 1 - да, 2 -нет ")
    if user_vacancy_storage == "1":
        storage_extention = input('1 - json | 2 - csv | 3 - txt')
        if storage_extention == "1":
            filename = input('Введите имя для JSON файла')
            save_json(vacancy_list, "data_storage/data/" + filename + ".json")
        elif storage_extention == "2":
            filename = input('Введите имя для CSV файла')
            save_csv(vacancy_list, "data_storage/data/" + filename + ".csv")
        elif storage_extention == "3":
            filename = input('Введите имя для TXT файла')
            save_txt(vacancy_list, "data_storage/data/" + filename + ".txt")
        else:
            print("Не верный ввод, повторите попытку")
            continue
    elif user_vacancy_storage == "2":
        print("Благодарим за пользование программой")
        break
