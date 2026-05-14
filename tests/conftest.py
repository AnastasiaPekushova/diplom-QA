import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.iu import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pymysql
from uuid import uuid4

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
        #host = "mysql",
        host = "localhost",
        user = "app",
        password = "pass",
        database ="app",
        cursorclass=pymysql.cursors.DictCursor
    )
    yield conn
    conn.close()

@pytest.fixture(scope="function") #Создание тестовых данных
def setup_test_data(sql_connect):
    payment_id = f"payment_{uuid4().hex[:8]}"
    credit_id = f"credit_{uuid4().hex[:8]}"
    order_id = f"order_{uuid4().hex[:8]}"

    with sql_connect.cursor() as cursor:
        cursor.execute("""
            insert into payment_entity (id, amount, created, status, transaction_id)
            values (%s, 1000, now(), 'APPROVED', %s)""",
            (payment_id, f"trans_{uuid4().hex[:8]}"))
        
        cursor.execute("""
            insert into credit_request_entity (id, bank_id, created, status)
            values (%s, %s, now(), 'APPROVED')""",
            (credit_id, f"bank_{uuid4().hex[:8]}"))
        
        cursor.execute("""
            insert into order_entity (id, created, credit_id, payment_id)
            values (%s, now(), 'NULL', %s)""",
            (order_id, payment_id))
        
        sql_connect.commit()

    yield

    with sql_connect.cursor() as cursor:
        cursor.execute("delete from order_entity where id = %s", (order_id,))
        cursor.execute("delete from payment_entity where id = %s", (payment_id,))
        cursor.execute("delete from credit_request_entity where id = %s", (credit_id,))
        sql_connect.commit()
