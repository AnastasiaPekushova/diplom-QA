*Запуск автотестов*

Для запуска автотестов необходимо:
1. Docker Desktop
2. Python
3. Google Chrome
4. Git

**Установка и запуск**

1. Клонировать реппозиторий:
В терминале ввести git clone https://github.com/AnastasiaPekushova/diplom-QA.git
2. Запустить приложение через Docker:
docker-compose up -d
3. После запуска контейнера приложение будет доступно по ссылке:
http://localhost:8080
4. Создать виртуальное окружение:
python -m venv venv
venv\Scripts\activate
5. Установить зависимости:
pip install -r requirements.txt
6. Запустить автотесты:
python -m pytest tests/ -v
7. Создать отчеты allure:
python -m pytest tests/ -v --alluredir=allure-result
allure serve allure-result
