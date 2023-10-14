from API import HeadHunterAPI, SuperJobAPI

if __name__ == "__main__":
    hh_api = HeadHunterAPI("https://api.hh.ru")
    superjob_api = SuperJobAPI("https://api.superjob.ru", API_KEY_SJ)

    json_data_storage = JSONDataStorage("vacancies.json")

    user_interaction()
