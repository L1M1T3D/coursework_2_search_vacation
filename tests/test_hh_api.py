from unittest.mock import patch

import pytest

from src.hh_api import HHVacancyAPI


class TestHHVacancyAPI:

    @pytest.fixture
    def api(self):
        return HHVacancyAPI()

    @patch("requests.get")
    def test_get_vacancies_success(self, mock_get, api):
        """Тест успешного получения данных с hh.ru"""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [{"name": "Software Engineer"}]}

        vacancies = api.get_vacancies("Software Engineer")

        assert len(vacancies["items"]) == 1
        assert vacancies["items"][0]["name"] == "Software Engineer"
        mock_get.assert_called_once_with(api.base_url, params={"text": "Software Engineer", "page": 0, "per_page": 20})

    @patch("requests.get")
    def test_get_vacancies_error(self, mock_get, api):
        """Тест обработки ошибки при получении данных с hh.ru"""
        mock_response = mock_get.return_value
        mock_response.status_code = 500

        with pytest.raises(Exception, match="Ошибка при получении данных с hh.ru"):
            api.get_vacancies("Software Engineer")
