from abc import ABC, abstractmethod

import requests


class VacanciesAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query, page=0, per_page=20):
        pass


class HHVacancyAPI(VacanciesAPI):
    """
    Получает список вакансий с платформы hh.ru по поисковому запросу.
    """

    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query, page=0, per_page=20):
        """Метод для получения вакансий по поисковому запросу"""
        params = {"text": search_query, "page": page, "per_page": per_page}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Ошибка при получении данных с hh.ru")
