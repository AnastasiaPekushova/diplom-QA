import pytest
import pymysql
import allure

@allure.epic("Тесты БД")
@allure.title("Платеж по карте одобрен, маскировка номера карты") 
def test_payment_approved_record_exists(sql_connect, setup_test_data):
    with sql_connect.cursor() as cursor:
        cursor.execute("SELECT * FROM payment_entity WHERE status = 'APPROVED' ORDER BY id DESC LIMIT 1")
        record = cursor.fetchone()

    assert record is not None, "Нет записи со статусом APPROVED в payment_entity"
    assert record.get("card_number") is None or "****" in str(record.get("card_number", "")), \
        f"Номер карты не замаскирован!"
    
@allure.epic("Тесты БД")
@allure.title("Кредит по данным карты одобрен, маскировка номера карты") 
def test_credit_approved_record_exists(sql_connect, setup_test_data):
    with sql_connect.cursor() as cursor:
        cursor.execute("SELECT * FROM credit_request_entity WHERE status = 'APPROVED' ORDER BY id DESC LIMIT 1")
        record = cursor.fetchone()

    assert record is not None, "Нет записи со статусом APPROVED в credit_request_entity"
    assert record.get("card_numder") is None or "****" in str(record.get("card_number", "")), \
        f"Номер карты не замаскирован!"