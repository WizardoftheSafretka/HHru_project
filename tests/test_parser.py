from unittest.mock import patch


from src.parser import HeadHunterAPI


@patch('requests.get')
def test_head_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'items': [{'id': '123', 'name': 'Developer'}]
    }

    api = HeadHunterAPI()
    api.load_vacancies('Developer')

    assert {'id': '123', 'name': 'Developer'} in api._HeadHunterAPI__vacancies

@patch('requests.get')
def test_head_api_300(mock_get):
    mock_get.return_value.status_code = 300
    mock_get.return_value.json.return_value = {
        'items': [{'id': '123', 'name': 'Developer'}]
    }

    api = HeadHunterAPI()
    api.load_vacancies('Developer')

    assert {'id': '123', 'name': 'Developer'} not in api._HeadHunterAPI__vacancies

