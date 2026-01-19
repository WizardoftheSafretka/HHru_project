import json
from unittest.mock import mock_open, patch

from src.save_file import SaveFile


def test_save_file_add(test_vacancy):
    with patch("builtins.open", mock_open()) as mocked_open:
        save_file = SaveFile(mocked_open)
        save_file.save_data(test_vacancy)
        mocked_open.assert_called_once_with("builtins.open", 'w', encoding="UTF-8")

def test_save_file_get(test_vacancy):
    test_data = json.dumps(test_vacancy)
    with patch("builtins.open", mock_open(read_data=test_data)) as mocked_open:
        save_file = SaveFile(mocked_open)
        result = save_file.get_data("builtins.open","Developer")
        assert result  == [{'name': 'Developer'}]
        mocked_open.assert_called_once_with("builtins.open", 'r', encoding='UTF-8')

def test_save_file_data(test_vacancy):
    test_data = json.dumps(test_vacancy)
    with patch("builtins.open", mock_open(read_data=test_data)) as mocked_open:
        save_file = SaveFile(mocked_open)
        save_file.del_data("builtins.open", "Developer")






