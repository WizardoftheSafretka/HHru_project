from unittest.mock import Mock, patch

from src.parser import HeadHunterAPI


@patch("requests.get")
def test_head_api(mock_get):
    hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    result = hh_api._api_connection()
    mock_get.assert_called_once_with(hh_api._url, headers=hh_api._headers, params=hh_api._params)
    assert result == mock_response


@patch("requests.get")
def test_head_api_error(mock_get):
    hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 300
    mock_get.return_value = mock_response
    result = hh_api._api_connection()
    mock_get.assert_called_once_with(hh_api._url, headers=hh_api._headers, params=hh_api._params)
    assert result is None


@patch("requests.get")
def test_load_vacancies(mock_get):
    hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": "123", "name": "Developer"}]}
    mock_get.return_value = mock_response
    hh_api._load_vacancies("Developer")
    mock_get.assert_called_with(hh_api._url, headers=hh_api._headers, params=hh_api._params)
    assert {"id": "123", "name": "Developer"} in hh_api._vacancies


@patch("requests.get")
def test_load_vacancies_empty(mock_get):
    hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response
    hh_api._load_vacancies("Developer")
    mock_get.assert_called_with(hh_api._url, headers=hh_api._headers, params=hh_api._params)
    assert hh_api._vacancies == []
