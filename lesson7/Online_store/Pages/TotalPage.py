from selenium.webdriver.common.by import By

class Total:

    def __init__(self, driver):

        self.browser = driver
        self.browser.get("https://www.saucedemo.com/checkout-step-two.html")
        self.browser.maximize_window()

    def total(self):

        self.total = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        self.total = self.total.strip().replace("Total: $", "")

        #assert total == "58.29"
        print(f"Итоговая сумма равна ${self.total}")