import json
from abc import ABC, abstractmethod


class AbstractWorkFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy, file_name):
        """Абстрактный метод для добавления вакансий"""

        pass

    @abstractmethod
    def get_data(self, file_name, keyword):
        """Абстрактный метод для получения данных"""

        pass

    @abstractmethod
    def del_info(self, file_name, name):
        """Абстрактный метод для удаления информации"""

        pass


class SaveFile(AbstractWorkFile):
    """Класс для сохранения информации о вакансиях"""

    def __init__(self, file_name='vacancy.json'):
        self.__file_name = file_name

    def add_vacancy(self, vacancy, file_name):
        """Метод для добавления вакансий"""

        data = vacancy
        with open(file_name, 'a', encoding="UTF-8") as f:
            json.dump(data, f)

    def get_data(self, file_name, keyword):
        """Метод для получения данных"""

        with open(file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        if "items" in data:
            return [item for item in data["items"] if keyword in item]
        else:
            return []

    def del_info(self, file_name, name):
        """Метод для удаления информации"""

        with open(file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        data["items"] = [item for item in data["items"] if item["name"] != name]
        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)




