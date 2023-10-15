class Currency():

    def __init__(self, value: int, currency: str):
        self.currency = currency
        self.value = value

    def __eq__(self, other):

        if not issubclass(other.__class__, Currency):
            raise TypeError('Нельзя сравнить!')
        return self.value == other.value

    def __le__(self, other):

        if not issubclass(other.__class__, Currency):
            raise TypeError('Нельзя сравнить!')
        return self.value <= other.value

    def __lt__(self, other):

        if not issubclass(other.__class__, Currency):
            raise TypeError('Нельзя сравнить!')
        return self.value < other.value

    def __str__(self):
        return f"{round(self.value)} {self.currency}"
