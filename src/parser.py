from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Абстрактный класс Parser
    """

    @abstractmethod
    def __init__(self, file_worker):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """
        Загрузить вакансии по ключевому слову с hh.ru
        :param keyword: ключевое слово для поиска вакансий
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json().get('items', [])
                if not vacancies:
                    break
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                print(f"Ошибка загрузки данных: {response.status_code}")
                break