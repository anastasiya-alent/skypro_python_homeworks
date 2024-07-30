from selenium.webdriver.common.by import By
class Authorization:

    def __init__(self, driver):
        self.browser = driver
        self.browser.get("https://www.saucedemo.com/")
        self.browser.maximize_window()

    def authorization(self): #ввод данных

        input_name = self.browser.find_element(By.ID, "user-name")
        input_name.send_keys("standard_user")

        input_password = self.browser.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")

    def click_button(self): #нажатие кнопки Login

        self.browser.find_element(By.ID, "login-button").click()