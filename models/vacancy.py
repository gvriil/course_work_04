from models.currency import Currency


class Vacancy:
    """
    Класс, представляющий информацию о вакансии.

    Attributes:
        title (str): Заголовок вакансии.
        link (str): Ссылка на вакансию.
        salary (Currency): Заработная плата для вакансии.
        description (str): Описание вакансии.
        town (str): Город, в котором размещена вакансия.

    Methods:
        __init__(self, title: str, link: str, salary: Currency, description: str, town: str): Конструктор класса.
        __repr__(self): Возвращает строковое представление вакансии.
        __eq__(self, other): Проверяет, равны ли зарплаты вакансий.
        __lt__(self, other): Сравнивает вакансии по зарплате (меньше).
        __le__(self, other): Сравнивает вакансии по зарплате (меньше или равно).
        get_dict(self): Возвращает вакансию в виде словаря.
        to_list(self): Возвращает вакансию в виде списка.

    Example:
    ```python
    vacancy = Vacancy("Python Developer", "https://example.com", Currency(60000, 'RUB'), "Python Developer job in Moscow", "Moscow")
    print(vacancy)
    if vacancy == other_vacancy:
        print("Зарплаты равны.")
    if vacancy < other_vacancy:
        print("Зарплата меньше.")
    ```
    """

    def __init__(self, title: str, link: str, salary: Currency, description: str, town: str):
        """
        Инициализирует объект Vacancy.

        Args:
            title (str): Заголовок вакансии.
            link (str): Ссылка на вакансию.
            salary (Currency): Заработная плата для вакансии.
            description (str): Описание вакансии.
            town (str): Город, в котором размещена вакансия.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.town = town

    def __repr__(self):
        """
        Возвращает строковое представление вакансии.

        Returns:
            str: Строковое представление вакансии.
        """
        return f"заголовок: {self.title}\n" \
               f"описание: {self.description}\n" \
               f"ссылка: {self.link}\n" \
               f"з/п: {self.salary}\n" \
               f"город: {self.town}\n"

    def __eq__(self, other):
        """
        Проверяет, равны ли зарплаты вакансий.

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если зарплаты равны, в противном случае False.
        """
        return self.salary == other.salary

    def __lt__(self, other):
        """
        Сравнивает вакансии по зарплате (меньше).

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если текущая вакансия имеет меньшую зарплату, в противном случае False.
        """
        if not issubclass(other.__class__, Vacancy):
            raise TypeError('Нельзя сравнить!')
        if self.salary is None:
            return True
        if other.salary is None:
            return False
        return self.salary < other.salary

    def __le__(self, other):
        """
        Сравнивает вакансии по зарплате (меньше или равно).

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если текущая вакансия имеет меньшую или равную зарплату, в противном случае False.
        """
        if not issubclass(other.__class__, Vacancy):
            raise TypeError('Нельзя сравнить!')
        if self.salary is None:
            return True
        if other.salary is None:
            return False
        return self.salary <= other.salary

    def get_dict(self):
        """
        Возвращает вакансию в виде словаря.

        Returns:
            dict: Словарь, представляющий вакансию.
        """
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

    def to_list(self):
        """
        Возвращает вакансию в виде списка.

        Returns:
            list: Список, представляющий вакансию.
        """
        return [self.town, self.link, self.salary, self.description, self.town]
