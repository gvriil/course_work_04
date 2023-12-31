# Вакансионный парсер

Этот проект представляет собой вакансионный парсер, который собирает информацию о вакансиях с разных платформ в России, сохраняет ее в файл и предоставляет удобный интерфейс для работы с ней (добавление, фильтрация, удаление).

## Что это такое?

**Парсинг** - это процесс сбора и систематизации данных из различных источников. Парсинг вакансий с веб-сайтов - распространенная задача для Python-разработчиков.

**API** (Application Programming Interface) - механизм, который позволяет программам взаимодействовать друг с другом, используя определенные правила.

## Задача

Создать программу, которая будет:

1. Получать информацию о вакансиях с разных платформ (например, hh.ru и superjob.ru) в России и СНГ.
2. Сохранять информацию о вакансиях в файл (JSON, CSV, или TXT).
3. Предоставлять возможности взаимодействия с вакансиями через консоль (например, поиск, фильтрация, сортировка).

## Как это работает?

1. Созданы абстрактные классы для работы с API разных платформ.
2. Реализованы классы, наследующиеся от абстрактного класса, для работы с конкретными платформами (например, HeadHunterAPI и SuperJobAPI).
3. Создан класс для работы с вакансиями (Vacancy), с методами сравнения вакансий и валидацией данных.
4. Определен абстрактный класс, обязывающий реализовать методы для сохранения, получения и удаления вакансий из файла.
5. Создан класс для сохранения информации о вакансиях в JSON-файл (другие форматы могут быть реализованы по желанию).

## Пример использования

```python
# Создание экземпляров классов для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
superjob_vacancies = superjob_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
json_saver.delete_vacancy(vacancy)

# Взаимодействие с пользователем через консоль
vacancy_finder()

# Начало работы программы выполняется через запуск
main.py
