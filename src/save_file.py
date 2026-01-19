import json
from abc import ABC, abstractmethod


class AbstractWorkFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_data(self, vacancy_list):
        """Абстрактный метод для сохранения вакансий"""

        pass

    @abstractmethod
    def get_data(self, keyword):
        """Абстрактный метод для получения данных"""

        pass

    @abstractmethod
    def del_data(self, keyword):
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
        data.update(new_data)
        with open(self.__file_name, 'w', encoding="UTF-8") as f:
            json.dump(data, f)

    def get_data(self, keyword):
        """Метод для получения данных по ключевому слову"""

        with open(self.__file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        result = []
        for item in data:
            if (keyword.lower() in item.get("name", "").lower() or
                    keyword.lower() in item.get("responsibility", "").lower()):
                result.append(item)
        return result

    def del_data(self, keyword):
        """Метод для удаления информации"""

        with open(self.__file_name, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        filtered_data = [
            item for item in data
            if (item.get("name", "").lower() != keyword.lower() and
                keyword.lower() not in item.get("responsibility", "").lower())
        ]
        with open(self.__file_name, 'w', encoding='UTF-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)




