class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("name", "alternate_url", "_salary", "responsibility")

    def __init__(self, name: str, alternate_url: str, salary: dict | int | None, responsibility: str):
        """Инициализация вакансии"""
        self.name = name
        self.alternate_url = alternate_url
        self._salary = self._validation(salary)
        self.responsibility = responsibility

    @staticmethod
    def _validation(salary_data):
        """Валидация и вычисление зарплаты."""
        if isinstance(salary_data, dict):
            from_salary = salary_data.get("from", 0) if isinstance(salary_data.get("from"), (int, float)) else 0
            to_salary = salary_data.get("to", 0) if isinstance(salary_data.get("to"), (int, float)) else 0
            count = (1 if from_salary else 0) + (1 if to_salary else 0)

            if count == 0:
                return 0
            return (from_salary + to_salary) / count
        elif isinstance(salary_data, (int, float)):
            return salary_data
        else:
            return 0

    @property
    def salary(self) -> int:
        """Геттер для зарплаты."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Сеттер для зарплаты."""
        self._salary = self._validation(value)  # Исправлено: добавлена правильная реализация сеттера

    def __str__(self) -> str:
        """Строковое представление вакансии."""
        return (
            f"Вакансия: {self.name}\n"
            f"Ссылка: {self.alternate_url}\n"
            f"Зарплата: {self._salary:.2f}\n"
            f"Описание: {self.responsibility[:100]}{'...' if len(self.responsibility) > 100 else ''}"
        )

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (<)."""
        if not isinstance(other, Vacancy):
            raise TypeError("Можно сравнивать только объекты Vacancy")
        return self._salary < other._salary

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (>)."""
        if not isinstance(other, Vacancy):
            raise TypeError("Можно сравнивать только объекты Vacancy")
        return self._salary > other._salary

    def __eq__(self, other: object) -> bool:
        """Проверка равенства вакансий по зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self._salary == other._salary

    def cast_to_dict(self) -> dict:
        """Преобразование вакансии в словарь."""
        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary": self._salary,
            "responsibility": self.responsibility,
        }
