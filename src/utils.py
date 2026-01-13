def filter_vacancies(vacancies_list: dict, filter_words: list[str]) -> list:
    """Функция для фильтраци вакансий"""

    return [item for item in vacancies_list["items"] if any(word in item["description"] for word in filter_words)]

def get_vacancies_by_salary(filtered_vacancies: list, salary_range: str) -> list:
    """Функция для получения вакансий по интервалу зарплаты"""

    salary_range_split = salary_range.split()
    salary_range_min = salary_range_split[0]
    salary_range_max = salary_range_split[1]
    return [item for item in filtered_vacancies if salary_range_max > item["salary"] > salary_range_min]

def sort_vacancies(ranged_vacancies: list)  -> list:
    """Фукнция для сортировки вакансий"""

    return  sorted(ranged_vacancies, key = lambda x: x["salary"])

def get_top_vacancies(sorted_vacancies: list, top_n: int) -> list:
    """Функция, возвращающая топ N вакансий"""

    return sorted_vacancies[0: top_n]
