# Sprint_9 — Автоматизация тестирования Foodgram

## О проекте

Этот проект содержит автоматизированные UI-тесты для веб-приложения Foodgram [https://foodgram-frontend-1.prakticum-team.ru](https://foodgram-frontend-1.prakticum-team.ru) — сервиса по созданию и обмену рецептами.

Тесты покрывают следующие сценарии:

- Создание аккаунта
- Авторизация пользователя
- Создание нового рецепта

Тесты написаны с использованием Selenium WebDriver, реализованы по паттерну Page Object и сопровождаются отчетами Allure.

## Технологии и инструменты

- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure Framework
- Docker (для контейнеризации тестов)
- Selenoid (для запуска браузеров в контейнерах)
- GitHub Actions (CI/CD)

## Структура проекта

```
Sprint_9/
├── pages/              # Page Object классы
├── tests/              # Тесты, сгруппированные по функционалу
├── locators/           # Локаторы
├── data.py             # Тестовые данные
├── conftest.py         # Фикстуры Pytest
├── Dockerfile          # Сборка Docker-образа с тестами
├── docker-compose.yml  # Конфигурация для Selenoid и тестов
├── .github/workflows/ci.yml # CI/CD workflow
└── README.md           # Текущий файл
```

## Установка зависимостей

Рекомендуется создать виртуальное окружение и установить зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Запуск тестов

### Локальный запуск

```bash
pytest --alluredir=allure-results
```

### Просмотр отчёта Allure

```bash
allure serve allure-results
```

### Запуск тестов через Docker и Selenoid

1. Собрать образ:

```bash
docker build -t sprint_9_tests .
```

2. Запустить Selenoid и тесты:

```bash
docker-compose up --build
```

