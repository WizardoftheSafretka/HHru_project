import json
import os
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

    def __init__(self, file_name="vacancy.json"):
        self.__file_name = file_name

    def save_data(self, vacancy_list):
        """Метод для сохранения вакансий"""
        if not isinstance(vacancy_list, list):
            vacancy_list = [vacancy_list]

        if os.path.exists(self.__file_name):
            with open(self.__file_name, "r", encoding="UTF-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
            data.extend(vacancy_list)

            with open(self.__file_name, "w", encoding="UTF-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        else:
            with open(self.__file_name, "w", encoding="UTF-8") as f:
                json.dump(vacancy_list, f, ensure_ascii=False, indent=4)

    def get_data(self, keyword):
        """Метод для получения данных по ключевому слову"""
        if not os.path.exists(self.__file_name):
            return []

        with open(self.__file_name, "r", encoding="UTF-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = [data]
        result = []
        for item in data:
            if (
                keyword.lower() in item.get("name", "").lower()
                or keyword.lower() in item.get("responsibility", "").lower()
            ):
                result.append(item)
        return result

    def del_data(self, keyword):
        """Метод для удаления информации"""
        if not os.path.exists(self.__file_name):
            return

        with open(self.__file_name, "r", encoding="UTF-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = [data]

        filtered_data = [
            item
            for item in data
            if (
                keyword.lower() not in item.get("name", "").lower()
                and keyword.lower() not in item.get("responsibility", "").lower()
            )
        ]

        with open(self.__file_name, "w", encoding="UTF-8") as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)
