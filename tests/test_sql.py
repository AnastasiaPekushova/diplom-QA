import pytest
import pymysql

#Дебетовая карта
def test_payment_approved_record_exists(sql_connect):
    with sql_connect.cursor() as cursor:
        cursor.execute("SELECT * FROM payment_entity WHERE status = 'APPROVED' ORDER BY id DESC LIMIT 1")
        record = cursor.fetchone()

    assert record is not None, "Нет записи со статусом APPROVED в payment_entity"
    assert record.get("card_number") is None or "****" in str(record.get("card_number", "")), \
        f"Номер карты не замаскирован!"
    
#Кредитная карта
def test_credit_approved_record_exists(sql_connect):
    with sql_connect.cursor() as cursor:
        cursor.execute("SELECT * FROM credit_request_entity WHERE status = 'APPROVED' ORDER BY id DESC LIMIT 1")
        record = cursor.fetchone()

    assert record is not None, "Нет записи со статусом APPROVED в credit_request_entity"
    assert record.get("card_numder") is None or "****" in str(record.get("card_number", "")), \
        f"Номер карты не замаскирован!"