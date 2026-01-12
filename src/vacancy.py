class Vacancy:
    name: str
    link: str
    salary: int
    description: str

    __slots__ = ('name', 'link', 'salary', 'description')

    def __init__(self, name, link, salary, description):
        if name:
            self.name = name
        else:
            raise ValueError("Имя не указано")
        if link:
            self.link = link
        else:
            raise ValueError("Ссылка не указана")
        if salary:
            self.salary = salary
        else:
            raise ValueError("Зарплата не указана")
        if description:
            self.description = description
        else:
            raise ValueError("Описание не указано")

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary



