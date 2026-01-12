import json
from abc import ABC, abstractmethod


class AbstractWorkFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self):
        """Абстрактный метод для добавления вакансий"""

        pass

    @abstractmethod
    def get_data(self):
        """Абстрактный метод для получения данных"""

        pass

    @abstractmethod
    def del_info(self):
        """Абстрактный метод для удаления информации"""

        pass

    @abstractmethod
    def save_file(self, vacancy, file_name):
        """Абстрактный метод для сохранения информации"""

        pass


class SaveFile(AbstractWorkFile):
    """Класс для сохранения информации о вакансиях"""

    def add_vacancy(self):
        """Метод для добавления вакансий"""
        pass

    def get_data(self):
        """Метод для получения данных"""

        pass

    def del_info(self):
        """Метод для удаления информации"""

        pass

    def save_file(self, vacancy, file_name):
        """Метод для сохранения информации"""

        data = vacancy
        with open('vacancy.json', 'a', encoding="UTF-8") as f:
            json.dump(data, f)
