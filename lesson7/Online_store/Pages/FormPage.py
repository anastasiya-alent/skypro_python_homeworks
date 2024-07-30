from selenium.webdriver.common.by import By

class Form:

    def __init__(self, driver):

        self.browser = driver
        self.browser.get("https://www.saucedemo.com/checkout-step-one.html")
        self.browser.maximize_window()

    def data_input(self): # заполняем данные

        name = self.browser.find_element(By.ID, "first-name")
        name.send_keys("Anastasiya")

        last_name = self.browser.find_element(By.ID, "last-name")
        last_name.send_keys("Alentieva")

        code = self.browser.find_element(By.ID, "postal-code")
        code.send_keys("344150")

    def click_continue(self): #нажимаем кнопку "continue"

        self.browser.find_element(By.ID, "continue").click()
        