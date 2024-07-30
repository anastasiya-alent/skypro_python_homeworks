from selenium.webdriver.common.by import By
class AddCart:

    def __init__(self, driver):
        self.browser = driver
        #self.browser.get("https://www.saucedemo.com/")
        self.browser.maximize_window()

    def add_cart(self):

        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    