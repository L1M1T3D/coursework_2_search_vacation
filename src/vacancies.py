class Vacancy:
    """
    Класс для представления вакансии.
    """

    def __init__(self, title: str, url: str, salary: int, description: str):
        self.title = title
        self.url = url
        self.salary = salary if salary is not None else 0
        self.description = description

    def __repr__(self):
        """Возвращает строковое представление объекта Vacancy."""
        return f"Vacancy(title={self.title}, salary={self.salary}, url={self.url})"

    def __eq__(self, other):
        """Сравнивает вакансии по зарплате."""
        return self.salary == other.salary

    def __lt__(self, other):
        """Сравнивает вакансии для сортировки по зарплате."""
        return self.salary < other.salary

    @staticmethod
    def validate_salary(salary_data):
        """Проверяет и возвращает зарплату из данных."""
        if salary_data and "from" in salary_data:
            return salary_data["from"]
        else:
            return 0
