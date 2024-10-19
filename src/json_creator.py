import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный класс для хранения вакансий.
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, filter_keyword: str = None, top_n: int = None):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_title: str):
        pass


class JSONVacancyStorage(VacancyStorage):
    """
    Класс для хранения вакансий в JSON-файле.
    """
    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в JSON-файл."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        vacancies.append(
            {"title": vacancy.title, "url": vacancy.url, "salary": vacancy.salary, "description": vacancy.description}
        )

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self, top_n=None, filter_keyword=None):
        """Получает список вакансий из JSON-файла с возможностью фильтрации."""
        with open(self.file_path, "r", encoding="utf-8") as f:
            vacancies = json.load(f)

        if filter_keyword:
            if isinstance(filter_keyword, str):
                filter_keyword = [filter_keyword]
            filter_keyword = [kw.lower() for kw in filter_keyword]

            def contains_keywords(vacancy_description):
                """Проверяет, содержатся ли все ключевые слова в описании вакансии."""
                description = vacancy_description.lower()
                return any(kw in description for kw in filter_keyword)

            vacancies = [v for v in vacancies if contains_keywords(v["description"])]

        vacancies.sort(key=lambda v: v["salary"], reverse=True)

        if top_n:
            vacancies = vacancies[:top_n]

        return [Vacancy(v["title"], v["url"], v["salary"], v["description"]) for v in vacancies]

    def delete_vacancy(self, vacancy_title: str):
        """Удаляет вакансию из JSON-файла по заголовку."""
        data = self._read_data()
        data = [v for v in data if v["title"] != vacancy_title]
        self._write_data(data)

    def _read_data(self):
        """Читает данные из JSON-файла."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file, ensure_ascii=False)
        except FileNotFoundError:
            return []

    def _write_data(self, data):
        """Записывает данные в JSON-файл."""
        with open(self.file_path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
