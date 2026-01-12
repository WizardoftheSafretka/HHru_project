

class Vacancy:
    name: str
    link: str
    salary: int
    description: str

    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        if salary:
            self.salary = salary
        else:
            self.salary = 0
        self.description = description


