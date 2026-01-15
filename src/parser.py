from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Абстрактный класс Parser
    """

    @abstractmethod
    def __init__(self):
        """Инициализация абстрактного класса Parser"""

        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        """Абстрактный метод получения вакансий"""

        pass

class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """Инициализация класса HH"""

        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def load_vacancies(self, keyword):
        """
        Загрузить вакансии по ключевому слову с hh.ru
        """

        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json().get('items', [])
                if not vacancies:
                    break
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                print(f"Ошибка загрузки данных: {response.status_code}")
                break