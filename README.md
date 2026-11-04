# API-тесты Reqres

Фреймворк для тестирования REST API [Reqres](https://reqres.in//): pytest, Pydantic, Faker, Allure, Docker и GitHub Actions.

## Подготовка

1. Python 3.11+
2. Виртуальное окружение и зависимости:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Скопируйте `.env.example` в `.env` и задайте `REQRES_API_KEY` (см. `.env.example`).

## Запуск тестов по окружениям

Окружение задаётся флагом `--env` (см. `conftest.py`): `dev` или `stage`.

**Локально (по умолчанию `stage`):**

```bash
pytest
```

**Явно dev:**

```bash
pytest --env=dev
```

**Stage:**

```bash
pytest --env=stage
```

Убедитесь, что для dev в `config/environments.py` задан корректный URL, если он отличается от stage.

Маркеры:

```bash
pytest -m smoke
pytest -m regression
```

## Запуск в Docker

Прогон тестов (папка `allure-results` очищается автоматически, результаты монтируются на хост):

```bash
docker compose run --rm tests
```

Смена окружения:

```bash
ENV=stage docker compose run --rm tests
ENV=dev docker compose run --rm tests

```

Просмотр Allure-отчёта локально (нужен [Allure Commandline](https://github.com/allure-framework/allure2/releases) и Java):

```bash
allure serve allure-results
```

Либо статический отчёт:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Параллельный прогон (pytest-xdist)

```bash
pytest -n auto
```

Можно комбинировать с окружением, например: `pytest --env=stage -n auto`.


Подробный вывод pytest локально: `pytest -v` (в `pytest.ini` по умолчанию без `-v`, чтобы не засорять CI).

## Allure (локально без Docker)

После прогона в каталоге `allure-results` появятся сырые данные отчёта (путь задан в `pyproject.toml` через `--alluredir`).

1. Установите [Allure Commandline](https://github.com/allure-framework/allure2/releases) и убедитесь, что команда `allure` доступна в `PATH` (нужна Java).
2. Откройте отчёт в браузере:

```bash
allure serve allure-results
```

Либо сгенерируйте статический отчёт и откройте `index.html`:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

В отчёте шаги описаны человекочитаемо: HTTP-запросы, проверки (assert) и валидация ответов по Pydantic-схемам.

## CI/CD (GitHub Actions)

Пайплайн описан в `.github/workflows/tests.yml`.

**Когда запускается:** на каждый `push`.

**Что делает:**

1. Собирает и запускает тесты (`Клонирует репозиторий, устанавливает зависимости и гоняет тесты`).
2. Генерирует Allure-отчёт из `allure-results`.
3. Сохраняет отчёт как artifact `allure-report` (хранение 14 дней).

**Как посмотреть отчёт из CI:**

1. Откройте вкладку Actions у репозитория.
2. Выберите успешный (или завершённый) workflow run.
3. Внизу страницы artifact с ссылкой на отчет
