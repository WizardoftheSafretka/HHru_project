import json
import os

from src.save_file import SaveFile


class TestSaveFile:

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.test_file = "test_vacancy.json"
        self.saver = SaveFile(self.test_file)

        # Тестовые данные
        self.vacancy1 = {
            "name": "Python Developer",
            "responsibility": "Разработка веб-приложений на Python",
            "salary": "100000-150000"
        }
        self.vacancy2 = {
            "name": "Java Developer",
            "responsibility": "Создание enterprise-решений",
            "salary": "120000-160000"
        }
        self.vacancy3 = {
            "name": "Data Scientist",
            "responsibility": "Анализ данных и машинное обучение на Python",
            "salary": "150000-200000"
        }

    def teardown_method(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_data_to_new_file(self):
        self.saver.save_data([self.vacancy1])
        assert os.path.exists(self.test_file)
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]["name"] == "Python Developer"

    def test_save_data_to_existing_file(self):
        self.saver.save_data([self.vacancy1])
        self.saver.save_data([self.vacancy2])
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert len(data) == 2
        assert data[0]["name"] == "Python Developer"
        assert data[1]["name"] == "Java Developer"

    def test_save_single_vacancy(self):
        self.saver.save_data(self.vacancy1)
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert isinstance(data, list)
        assert len(data) == 1

    def test_save_empty_list(self):
        self.saver.save_data([])
        assert os.path.exists(self.test_file)
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert data == []

    def test_get_data_by_keyword_in_name(self):
        self.saver.save_data([self.vacancy1, self.vacancy2, self.vacancy3])
        result = self.saver.get_data("Python")
        assert len(result) == 2
        names = [item["name"] for item in result]
        assert "Python Developer" in names
        assert "Data Scientist" in names

    def test_get_data_by_keyword_in_responsibility(self):
        self.saver.save_data([self.vacancy1, self.vacancy2])
        result = self.saver.get_data("разработка")
        assert len(result) == 1
        assert result[0]["name"] == "Python Developer"

    def test_get_data_case_insensitive(self):
        self.saver.save_data([self.vacancy1])
        result_lower = self.saver.get_data("python")
        result_upper = self.saver.get_data("PYTHON")
        result_mixed = self.saver.get_data("PyThOn")
        assert len(result_lower) == 1
        assert len(result_upper) == 1
        assert len(result_mixed) == 1

    def test_get_data_no_matches(self):
        self.saver.save_data([self.vacancy1])
        result = self.saver.get_data("JavaScript")
        assert result == []

    def test_get_data_from_empty_file(self):
        self.saver.save_data([])
        result = self.saver.get_data("Python")
        assert result == []

    def test_get_data_file_not_exists(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        result = self.saver.get_data("Python")
        assert result == []

    def test_del_data_by_keyword(self):
        self.saver.save_data([self.vacancy1, self.vacancy2, self.vacancy3])
        self.saver.del_data("Python")
        result = self.saver.get_data("Python")
        assert len(result) == 0
        remaining = self.saver.get_data("")
        assert len(remaining) == 1
        assert remaining[0]["name"] == "Java Developer"

    def test_del_data_partial_match(self):
        self.saver.save_data([self.vacancy1])
        self.saver.del_data("Dev")
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert len(data) == 0

    def test_del_data_nothing_to_delete(self):
        self.saver.save_data([self.vacancy1])
        self.saver.del_data("JavaScript")
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)

        assert len(data) == 1
        assert data[0]["name"] == "Python Developer"

    def test_del_data_from_empty_file(self):
        self.saver.save_data([])
        self.saver.del_data("Python")
        with open(self.test_file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        assert data == []

    def test_del_data_file_not_exists(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.saver.del_data("Python")