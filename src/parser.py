from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный класс Parser
    """

    @abstractmethod
    def _api_connection(self):
        """Абстрактный метод подключения к API"""

        pass

    @abstractmethod
    def _load_vacancies(self, keyword):
        """Абстрактный метод получения вакансий"""

        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """Инициализация класса HH"""

        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "page": 0, "per_page": 100}
        self._vacancies = []

    def _api_connection(self):
        """Метод подключения к API"""
        response = requests.get(self._url, headers=self._headers, params=self._params)
        if response.status_code == 200:
            return response
        else:
            print(f"Ошибка загрузки данных: {response.status_code}")
            return None

    def _load_vacancies(self, keyword):
        """
        Загрузить вакансии по ключевому слову с hh.ru
        """
        self._params["text"] = keyword
        while self._params.get("page") != 20:
            response = self._api_connection()
            vacancies = response.json().get("items", [])
            if not vacancies:
                break
            self._vacancies.extend(vacancies)
            self._params["page"] += 1
