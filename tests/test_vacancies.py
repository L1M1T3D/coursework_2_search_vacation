from src.vacancies import Vacancy


class TestVacancy:

    def test_init(self):
        vacancy = Vacancy("Software Engineer", "https://example.com", 100000, "Лучшая работа на планете!!!")
        assert vacancy.title == "Software Engineer"
        assert vacancy.url == "https://example.com"
        assert vacancy.salary == 100000
        assert vacancy.description == "Лучшая работа на планете!!!"

    def test_init_with_none_salary(self):
        vacancy = Vacancy("Software Engineer", "https://example.com", None, "Лучшая работа на планете!!!")
        assert vacancy.salary == 0

    def test_repr(self):
        vacancy = Vacancy("Software Engineer", "https://example.com", 100000, "Лучшая работа на планете!!!")
        assert repr(vacancy) == "Vacancy(title=Software Engineer, salary=100000, url=https://example.com)"

    def test_eq(self):
        vacancy1 = Vacancy("Software Engineer", "https://example.com", 100000, "Лучшая работа на планете!!!")
        vacancy2 = Vacancy("Data Scientist", "https://example.com", 100000, "Лучшая работа на планете!!!")
        assert vacancy1 == vacancy2

    def test_lt(self):
        vacancy1 = Vacancy("Software Engineer", "https://example.com", 100000, "Лучшая работа на планете!!!")
        vacancy2 = Vacancy("Data Scientist", "https://example.com", 150000, "Лучшая работа на планете!!!")
        assert vacancy1 < vacancy2

    def test_validate_salary_with_data(self):
        salary_data = {"from": 50000}
        assert Vacancy.validate_salary(salary_data) == 50000

    def test_validate_salary_without_data(self):
        salary_data = None
        assert Vacancy.validate_salary(salary_data) == 0
