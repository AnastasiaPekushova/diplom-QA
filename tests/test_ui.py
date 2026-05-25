
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("UI-тесты")
@allure.title(" Оплата по карте 4444 4444 4444 44441 ")
def test_payment_approved_debet(brauser, base_url,valid_data,card_data):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить']"))).click()

    with allure.step("Жду поле ввода номера карты"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))

    with allure.step("2. Заполняю карту"):
        card_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_input.clear()
        card_input.send_keys(card_data["approved_card"])
    
    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
       year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
       year_input.clear()
       year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])
  
    with allure.step("6. Заполняю cvc код"):
       cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
       cvc_input.clear()
       cvc_input.send_keys(valid_data["cvc"])

    with allure.step("7. Нахожу и кликаю продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Жду уведомление"):
        success_message = WebDriverWait(brauser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".notification_status_ok")))
    
    with allure.step("9. Проверяю уведомление"):
       assert "Успешно" in success_message.text 
    
   
@allure.epic("UI-тесты")
@allure.title(" Кредит по данным карты 4444 4444 4444 44441 ") 
def test_payment_approved_credit(brauser, base_url,valid_data,card_data):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить в кредит"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить в кредит']"))).click()
        print("жду поле ввода номера карты")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))
    
    with allure.step("2. Заполняю карту"):
        card_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_input.clear()
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("6. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])
    
    with allure.step("7. Нахожу и кликаю продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Жду уведомление"):
        success_message = WebDriverWait(brauser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".notification_status_ok")))

    with allure.step("9. Проверяю уведомление"):
        assert "Успешно" in success_message.text


@allure.epic("UI-тесты")
@allure.title(" Оплата по карте 4444 4444 4444 44442 ")
def test_payment_declined_debet(brauser, base_url, valid_data, card_data):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить']"))).click()
    with allure.step("жду поле ввода номера карты"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))
    
    with allure.step("2. Заполняю карту"):
        card_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_input.clear()
        card_input.send_keys(card_data["declined_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("6. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])
    
    with allure.step("7. Нахожу и кликаю продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Жду уведомление"):
        error_message = WebDriverWait(brauser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".notification_status_error")))

    with allure.step("9. Проверяю уведомление"):
        assert "Ошибка" in error_message.text


@allure.epic("UI-тесты")
@allure.title(" Кредит по данным карты 4444 4444 4444 44442 ") 
def test_payment_declined_credit(brauser, base_url, valid_data, card_data):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить в кредит"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить в кредит']"))).click()
    with allure.step("жду поле ввода номера карты"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))
    
    with allure.step("2. Заполняю карту"):
        card_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_input.clear()
        card_input.send_keys(card_data["declined_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("6. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])
    
    with allure.step("7. Нахожу и кликаю продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Жду уведомление"):
        error_message = WebDriverWait(brauser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".notification_status_error")))

    with allure.step("9. Проверяю уведомление"):
        assert "Ошибка" in error_message.text
