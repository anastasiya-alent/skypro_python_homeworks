from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    search_input_f = driver.find_element(By.CSS_SELECTOR, '#delay')
    search_input_f.clear()
    search_input_f.send_keys("45")

    driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    result_text = driver.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"
