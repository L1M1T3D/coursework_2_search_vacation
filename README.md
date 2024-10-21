
# Проект "Управление вакансиями"

## Описание

Этот проект предназначен для работы с вакансиями с платформы [hh.ru](https://hh.ru). С помощью программы можно искать вакансии по заданному запросу, сохранять их в JSON-файл, сортировать по зарплате и фильтровать по ключевым словам.

## Функционал

- **Поиск вакансий** по ключевому слову через API hh.ru.
- **Сохранение вакансий** в формате JSON для дальнейшей работы.
- **Фильтрация вакансий** по ключевым словам в описании.
- **Вывод топ N вакансий** с наивысшей зарплатой.

## Требования

Для запуска проекта вам потребуется:

- **Python** 3.8 и выше
- **Библиотеки**:
  - `requests`
  - `pytest`

Все необходимые зависимости можно установить с помощью команды:

```bash
pip install -r requirements.txt
```

## Установка и запуск

1. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Запуск программы**:
   ```bash
   python main.py
   ```

   Программа предложит ввести поисковый запрос для поиска вакансий, количество вакансий для вывода по зарплате и ключевые слова для фильтрации.

## Пример использования

1. При запуске программы вам предложат ввести запрос для поиска вакансий. Например, введите:
   ```
   Введите поисковый запрос для вакансий: Python разработчик
   ```

2. После этого программа сохранит вакансии в файл `vacancies.json` и спросит, сколько вакансий вы хотите увидеть в списке по зарплате:
   ```
   Введите количество вакансий для отображения по зарплате: 5
   ```

3. В следующем шаге можно ввести ключевые слова для фильтрации вакансий по описанию:
   ```
   Введите ключевые слова для поиска вакансий (через запятую): senior, django
   ```

4. Если найдутся вакансии с этими ключевыми словами, они будут выведены на экран. Если нет, программа сообщит, что такие вакансии не найдены.

## Тестирование

В проекте реализовано тестирование с использованием библиотеки **pytest**. Для запуска тестов и просмотра покрытия кода тестами выполните команды:

```bash
pytest
pytest --cov=src --cov-report=html
```

Тесты покрывают функционал работы с API и манипуляции вакансиями.

## Структура проекта

```
vacancy_project/
│
├── data/
├── src/
│   ├── hh_api.py               # Класс для работы с API hh.ru
│   ├── vacancies.py            # Класс для работы с вакансиями
│   ├── json_storage.py         # Класс для сохранения вакансий в JSON
│
├── tests/
│   ├── test_hh_api.py          # Тесты для работы с API hh.ru
│   ├── test_vacancies.py       # Тесты для работы с вакансиями
│
├── main.py                     # Основная программа для взаимодействия с пользователем
├── pyproject.toml              # Конфигурация проекта
├── README.md                   # Описание проекта
├── requirements.txt            # Список зависимостей
├── vacancies.json              # Файл с сохраненными вакансиями
```

## Разработчик проекта

**Илья Топко** — миллиардер, плейбой, филантроп
