from selenium.webdriver.common.by import By

class Cart:

    def __init__(self, driver):

        self.browser = driver
        self.browser.get("https://www.saucedemo.com/cart.html")
        self.browser.maximize_window()

    def click_checkout(self):

        self.browser.find_element(By.ID, "checkout").click()

    