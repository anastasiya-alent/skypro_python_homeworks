from selenium.webdriver.common.by import By
from data import *

class FirstPage:
    def __init__(self, driver):
        self.browser = driver
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.browser.maximize_window()

    def find_filds(self): #находим поля
        self.first_name = (By.CSS_SELECTOR, '[name="first-name"]')
        self.last_name = (By.CSS_SELECTOR, '[name="last-name"]')
        self.address = (By.CSS_SELECTOR, '[name="address"]')
        self.zip_code = (By.CSS_SELECTOR, '[name="zip-code"]')
        self.city = (By.CSS_SELECTOR, '[name="city"]')
        self.country = (By.CSS_SELECTOR, '[name="country"]')
        self.email = (By.CSS_SELECTOR, '[name="e-mail"]')
        self.phone = (By.CSS_SELECTOR, '[name="phone"]')
        self.job_position = (By.CSS_SELECTOR, '[name="job-position"]')
        self.company = (By.CSS_SELECTOR, '[name="company"]')

    def send_keys(self): #подставляем значения
        self.browser.find_element(*self.first_name).send_keys(first_name)
        self.browser.find_element(*self.last_name).send_keys(last_name)
        self.browser.find_element(*self.address).send_keys(address)
        self.browser.find_element(*self.zip_code).send_keys(zip_code)
        self.browser.find_element(*self.city).send_keys(city)
        self.browser.find_element(*self.country).send_keys(country)
        self.browser.find_element(*self.email).send_keys(email)
        self.browser.find_element(*self.phone).send_keys(phone)
        self.browser.find_element(*self.job_position).send_keys(job_position)
        self.browser.find_element(*self.company).send_keys(company)

    def click_Submit(self): #нажимаем кнопку
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
 