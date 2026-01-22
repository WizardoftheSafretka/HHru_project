import pytest

from src.vacancy import Vacancy


class TestVacancy:
    def test_init_with_valid_dict_salary(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка на Python",
        )

        assert vacancy.name == "Python Developer"
        assert vacancy.alternate_url == "https://hh.ru/vacancy/123"
        assert vacancy.responsibility == "Разработка на Python"
        assert vacancy.salary == 125000.0

    def test_init_with_none_salary(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary=None,
            responsibility="Разработка на Python",
        )

        assert vacancy.salary == 0

    def test_init_with_int_salary(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary=120000,
            responsibility="Разработка на Python",
        )

        assert vacancy.salary == 120000

    def test_init_with_partial_dict_salary(self):
        vacancy1 = Vacancy(
            name="Developer 1",
            alternate_url="https://hh.ru/vacancy/1",
            salary={"from": 100000, "to": None},
            responsibility="Разработка",
        )
        assert vacancy1.salary == 100000

        vacancy2 = Vacancy(
            name="Developer 2",
            alternate_url="https://hh.ru/vacancy/2",
            salary={"from": None, "to": 150000},
            responsibility="Разработка",
        )
        assert vacancy2.salary == 150000

        vacancy3 = Vacancy(
            name="Developer 3",
            alternate_url="https://hh.ru/vacancy/3",
            salary={"from": None, "to": None},
            responsibility="Разработка",
        )
        assert vacancy3.salary == 0

    def test_validation_edge_cases(self):

        vacancy = Vacancy(
            name="Developer", alternate_url="https://hh.ru/vacancy/123", salary={}, responsibility="Разработка"
        )
        assert vacancy.salary == 0

        vacancy = Vacancy(
            name="Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary={"from": "100000", "to": "150000"},
            responsibility="Разработка",
        )
        assert vacancy.salary == 0

    def test_salary_property(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка на Python",
        )

        assert isinstance(vacancy.salary, float)
        assert vacancy.salary == 125000

    def test_str_method(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка на Python, Django, Flask. Требования: опыт от 3 лет.",
        )

        result = str(vacancy)
        assert "Вакансия: Python Developer" in result
        assert "Ссылка: https://hh.ru/vacancy/123" in result
        assert "Зарплата: 125000.00" in result
        assert "Описание: Разработка на Python, Django, Flask. Требования: опыт от 3 лет." in result

    def test_comparison_operators(self):
        """Тест операторов сравнения."""
        vacancy1 = Vacancy(
            name="Junior",
            alternate_url="https://hh.ru/vacancy/1",
            salary={"from": 50000, "to": 70000},
            responsibility="Разработка",
        )

        vacancy2 = Vacancy(
            name="Middle",
            alternate_url="https://hh.ru/vacancy/2",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка",
        )

        vacancy3 = Vacancy(
            name="Middle 2",
            alternate_url="https://hh.ru/vacancy/3",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка",
        )

        assert vacancy1 < vacancy2
        assert not vacancy2 < vacancy1

        assert vacancy2 > vacancy1
        assert not vacancy1 > vacancy2

        assert vacancy2 == vacancy3
        assert not vacancy1 == vacancy2

    def test_comparison_with_wrong_type(self):
        vacancy = Vacancy(
            name="Developer",
            alternate_url="https://hh.ru/vacancy/1",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка",
        )

        with pytest.raises(TypeError, match="Можно сравнивать только объекты Vacancy"):
            vacancy < "not a vacancy"

        with pytest.raises(TypeError, match="Можно сравнивать только объекты Vacancy"):
            vacancy > 123

        assert vacancy.__eq__("not a vacancy") == NotImplemented

    def test_cast_to_dict(self):
        vacancy = Vacancy(
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/123",
            salary={"from": 100000, "to": 150000},
            responsibility="Разработка на Python",
        )

        result = vacancy.cast_to_dict()

        assert isinstance(result, dict)
        assert result["name"] == "Python Developer"
        assert result["alternate_url"] == "https://hh.ru/vacancy/123"
        assert result["salary"] == 125000
        assert result["responsibility"] == "Разработка на Python"
        assert len(result) == 4
