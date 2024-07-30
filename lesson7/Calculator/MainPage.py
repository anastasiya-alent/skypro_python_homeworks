from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MainPageCal:

    def __init__(self, driver):
        self.browser = driver
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.browser.maximize_window()

    def input_time(self): # находим поле и вводим значение 45
        entry_field = self.browser.find_element(By.CSS_SELECTOR, '#delay')
        entry_field.clear()
        entry_field.send_keys("45")

    def entering_values_click(self): #клик на элементы калькулятора
        self.browser.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def checking_value(self): # ожидаем появление результата, выводим текст результата
        
        WebDriverWait(self.browser, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        return self.browser.find_element(By.CLASS_NAME, "screen").text




