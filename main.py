from src.hh_api import HHVacancyAPI
from src.json_creator import JSONVacancyStorage
from src.vacancies import Vacancy


def user_interaction():
    """
    Функция для взаимодействия с пользователем, в которой пользователь последовательно вводит данные
    для поиска вакансий, получения топа по зарплате и поиска по ключевым словам.
    """
    api = HHVacancyAPI()
    storage = JSONVacancyStorage()

    query = input("Введите поисковый запрос для вакансий: ")
    vacancies_data = api.get_vacancies(query)
    for item in vacancies_data["items"]:
        salary = Vacancy.validate_salary(item["salary"])
        vacancy = Vacancy(item["name"], item["alternate_url"], salary, item["snippet"]["requirement"])
        storage.add_vacancy(vacancy)
    print("Вакансии сохранены в файл.")

    n = int(input("Введите количество вакансий для отображения по зарплате: "))
    top_vacancies = storage.get_vacancies(top_n=n)
    print(f"\nТоп {n} вакансий по зарплате:")
    for v in top_vacancies:
        print(v)

    keywords = input("\nВведите ключевые слова для поиска вакансий (через запятую): ").split(",")
    keywords = [kw.strip() for kw in keywords]
    filtered_vacancies = storage.get_vacancies(filter_keyword=keywords)
    if not filtered_vacancies:
        print(f"\nВакансии, содержащие ключевые слова: {', '.join(keywords)} не найдены.")
    else:
        print(f"\nВакансии, содержащие ключевые слова: {', '.join(keywords)}")
        for v in filtered_vacancies:
            print(v)


if __name__ == "__main__":
    user_interaction()
