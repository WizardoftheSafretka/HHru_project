class Vacancy:
    name: str
    alternate_url: str
    salary: int
    responsibility: str

    __slots__ = ('name', 'alternate_url', '_salary', 'responsibility')

    def __init__(self, name, alternate_url, salary, responsibility):
            self.name = name
            self.alternate_url = alternate_url
            self._salary = salary
            self.responsibility = responsibility

    @property
    def salary(self):
        """Геттер для salary. Возвращает 0 если salary = None."""
        return self._salary if isinstance(self._salary, int) else 0

    @salary.setter
    def salary(self, value):
        """Сеттер для salary. Хранит исходное значение."""
        self._salary = value



    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def cast_to_dict(self):
        return {"name": self.name, "alternate_url": self.alternate_url, "salary": self._salary}



