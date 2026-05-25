import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Тесты для кнопки 'Купить'")
@allure.title("Валидация поля номер карты") 
@allure.description("Поле номер карты")
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("123456789012345", "Неверный формат", "validation"), ("12345678901234567", "Неверный формат", "len")])
def test_card_number_validation_debet(brauser, base_url, valid_data, invalid_data, error_text, type):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить']"))).click()
    with allure.step("жду поле ввода номера карты"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))

    with allure.step("2. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("3. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля номер карты"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 16

@allure.epic("Тесты для кнопки 'Купить'")
@allure.title("Валидация поля месяц") 
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("1", "Неверный формат", "validation"), ("123", "Неверный формат", "len"), ("13", "Неверно указан срок действия карты", "validation"), ("00", "Неверно указан срок действия карты", "validation")])
def test_month_validation_debet(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля месяц"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 2

@allure.epic("Тесты для кнопки 'Купить'")
@allure.title("Валидация поля год") 
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("1", "Неверный формат", "validation"), ("123", "Неверный формат", "len"), ("25", "Истёк срок действия карты", "validation")])
def test_year_validation_debet(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля год"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 2

@allure.epic("Тесты для кнопки 'Купить'")
@allure.title("Валидация поля владелец") 
@pytest.mark.parametrize("invalid_data, error_text", [("", "Поле обязательно для заполнения"), ("123", "Неверный формат"), ("!№;", "Неверный формат"), ("N", "Неверный формат"), ("Д", "Неверный формат")])
def test_owner_validation_debet(brauser, base_url, valid_data, invalid_data, error_text, card_data):
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
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля владелец"):
        card_field = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка ответа"):
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
        assert error_text in error.text

@allure.epic("Тесты для кнопки 'Купить'")
@allure.title("Валидация поля CVC/CVV") 
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("12", "Неверный формат", "validation"), ("1234", "Неверный формат", "len"), ("000", "Неверный формат", "validation")])
def test_cvc_validation_debet(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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

    with allure.step("6. Невалидные данные для поля cvc"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='CVC/CVV']/ancestor::span[contains(@class,'input-group__input-case')]//span[@class='input__sub']")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 3


@allure.epic("Тесты для кнопки 'Купить в кредит'")
@allure.title("Валидация поля номер карты") 
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("123456789012345", "Неверный формат", "validation"), ("12345678901234567", "Неверный формат", "len")])
def test_card_number_validation_credit(brauser, base_url, valid_data, invalid_data, error_text, type):
    with allure.step("Запуск браузера"):
        brauser.get(base_url)
        wait = WebDriverWait(brauser, 15)

    with allure.step("1. Ищу кнопку купить в кредит"):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Купить в кредит']"))).click()
    with allure.step("жду поле ввода номера карты"):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')))

    with allure.step("2. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("3. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля номер карты"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 16

@allure.epic("Тесты для кнопки 'Купить в кредит'")
@allure.title("Валидация поля месяц")
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("1", "Неверный формат", "validation"), ("123", "Неверный формат", "len"), ("13", "Неверно указан срок действия карты", "validation"), ("00", "Неверно указан срок действия карты", "validation")])
def test_month_validation_credit(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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
        card_input.send_keys(card_data["approved_card"])
    
    with allure.step("3. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля месяц"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 2

@allure.epic("Тесты для кнопки 'Купить в кредит'")
@allure.title("Валидация поля год")
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("1", "Неверный формат", "validation"), ("123", "Неверный формат", "len"), ("25", "Истёк срок действия карты", "validation")])
def test_year_validation_credit(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю владелец"):
        owner_input = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        owner_input.clear()
        owner_input.send_keys(valid_data["owner"])

    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля год"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 2

@allure.epic("Тесты для кнопки 'Купить в кредит'")
@allure.title("Валидация поля владелец")
@pytest.mark.parametrize("invalid_data, error_text", [("", "Поле обязательно для заполнения"), ("123", "Неверный формат"), ("!№;", "Неверный формат"), ("N", "Неверный формат"), ("Д", "Неверный формат")])
def test_owner_validation_credit(brauser, base_url, valid_data, invalid_data, error_text, card_data):
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
        card_input.send_keys(card_data["approved_card"])

    with allure.step("3. Заполняю месяц"):
        month_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="08"]')
        month_input.clear()
        month_input.send_keys(valid_data["mont"])
    
    with allure.step("4. Заполняю год"):
        year_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="22"]')
        year_input.clear()
        year_input.send_keys(valid_data["year"])
    
    with allure.step("5. Заполняю cvc код"):
        cvc_input = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        cvc_input.clear()
        cvc_input.send_keys(valid_data["cvc"])

    with allure.step("6. Невалидные данные для поля владелец"):
        card_field = brauser.find_element(By.XPATH, "//span[text()='Владелец']/following-sibling::span//input")
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка ответа"):
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input__sub")))
        assert error_text in error.text

@allure.epic("Тесты для кнопки 'Купить в кредит'")
@allure.title("Валидация поля CVC/CVV")
@pytest.mark.parametrize("invalid_data, error_text, type", [("", "Неверный формат", "validation"), ("карта", "Неверный формат", "validation"), ("carta", "Неверный формат", "validation"), ("!@#", "Неверный формат", "validation"), ("12", "Неверный формат", "validation"), ("1234", "Неверный формат", "len"), ("000", "Неверный формат", "validation")])
def test_cvc_validation_credit(brauser, base_url, valid_data, invalid_data, error_text, type, card_data):
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

    with allure.step("6. Невалидные данные для поля cvc"):
        card_field = brauser.find_element(By.CSS_SELECTOR, 'input[placeholder="999"]' )
        card_field.clear()
        card_field.send_keys(invalid_data)

    with allure.step("7. Кликнуть продолжить"):
        continue_button = brauser.find_element(By.CSS_SELECTOR, "form .button_view_extra")
        continue_button.click()

    with allure.step("8. Проверка типа параметризации"):
        if type == "validation":
            error = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='CVC/CVV']/ancestor::span[contains(@class,'input-group__input-case')]//span[@class='input__sub']")))
            assert error_text in error.text

        elif type == "len":
            now = card_field.get_attribute("value").replace(" ", "")
            assert len(now) == 3