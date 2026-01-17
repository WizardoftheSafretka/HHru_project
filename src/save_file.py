import json
from abc import ABC, abstractmethod


class AbstractWorkFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_data(self, vacancy_list):
        """Абстрактный метод для сохранения вакансий"""

        pass

    @abstractmethod
    def get_data(self, file_name, keyword):
        """Абстрактный метод для получения данных"""

        pass

    @abstractmethod
    def del_data(self, file_name, name):
        """Абстрактный метод для удаления информации"""

        pass


class SaveFile(AbstractWorkFile):
    """Класс для сохранения информации о вакансиях"""

    def __init__(self, file_name='vacancy.json'):
        self.__file_name = file_name

    def save_data(self, vacancy_list):
        """Метод для сохранения вакансий"""

        with open(self.__file_name, 'r', encoding="UTF-8") as f:
            data = json.load(f)
        new_data = vacancy_list
        result_data_dict = {}
        for d in data + new_data:
            result_data_dict[d["alternate_url"]] = d

        result = list(result_data_dict.values())

        with open(self.__file_name, 'w', encoding="UTF-8") as f:
            json.dump(f, result)

    def get_data(self, file_name, keyword):
        """Метод для получения данных"""

        with open(file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        if "items" in data:
            return [item for item in data["items"] if keyword in item["name"]]
        else:
            return []

    def del_info(self, file_name, name):
        """Метод для удаления информации"""

        with open(file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        data["items"] = [item for item in data["items"] if item["name"] != name]
        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)




