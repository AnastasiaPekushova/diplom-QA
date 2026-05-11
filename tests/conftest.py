import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.iu import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pymysql

@pytest.fixture() # Валидные данные для заполнения формы
def valid_data():
    return {
        "mont": "08",
        "year": "27",
        "owner": "Иван Петров",
        "cvc": "999"
    }

@pytest.fixture() # Создание и настройка браузера
def brauser():
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage") 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

@pytest.fixture() # url приложения
def base_url():
    return "http://localhost:8080"

@pytest.fixture() # Данные карт
def card_data():
    return {
        "approved_card": "4444 4444 4444 4441",
        "declined_card": "4444 4444 4444 4442"
    }

@pytest.fixture(scope="session") # Подключение к БД
def sql_connect():
    conn = pymysql.connect(
        host = "localhost",
        user = "app",
        password = "pass",
        database ="app",
        cursorclass=pymysql.cursors.DictCursor
    )
    yield conn
    conn.close()