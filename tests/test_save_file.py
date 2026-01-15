import json
from unittest.mock import mock_open, patch

from src.save_file import SaveFile


def test_save_file_add(test_vacancy):
    with patch("builtins.open", mock_open()) as mocked_open:
        save_file = SaveFile()
        save_file.add_vacancy(test_vacancy)
        mocked_open.assert_called_once_with('vacancy.json', 'a', encoding="UTF-8")

def test_save_file_get(test_vacancy):
    test_data = json.dumps(test_vacancy)
    with patch("builtins.open", mock_open(read_data=test_data)) as mocked_open:
        save_file = SaveFile("test")
        result = save_file.get_data("test","Developer")
        assert result  == [{'name': 'Developer'}]
        mocked_open.assert_called_once_with("test", 'r', encoding='UTF-8')

def test_save_file_info(test_vacancy):
    test_data = json.dumps(test_vacancy)
    with patch("builtins.open", mock_open(read_data=test_data)) as mocked_open:
        save_file = SaveFile("test")
        save_file.del_info("test", "Developer")






