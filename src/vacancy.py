class Vacancy:
    name: str
    alternate_url: str
    salary: int
    responsibility: str

    __slots__ = ('name', 'alternate_url', '_salary', 'responsibility')

    def __str__(self):
        return f"name: {self.name}, alternate_url: {self.alternate_url}, salary: {self._salary}, responsibility: {self.responsibility}"

    def __init__(self, name, alternate_url, salary, responsibility):
            self.name = name
            self.alternate_url = alternate_url
            self._salary = self.validation(salary)
            self.responsibility = responsibility

    @staticmethod
    def validation(x):
        return (x["from"] if isinstance(x["from"], int) else 0 +x["to"]
        if isinstance(x["to"], int) else 0)/(bool(x["from"])+bool(x["to"])) \
            if isinstance(x, dict) else 0

    def __lt__(self, other):
        return self._salary < other._salary

    def __gt__(self, other):
        return self._salary > other._salary

    def __eq__(self, other):
        return self._salary == other._salary

    def cast_to_dict(self):
        return {"name": self.name, "alternate_url": self.alternate_url, "salary": self._salary, "responsibility": self.responsibility}

if __name__ == "__main__":
    exp_1 = Vacancy("test", "www", None, "responsibility")
    print(exp_1)

