from selenium.webdriver.common.by import By
from data import *

class SecondPage:
    def __init__(self, driver):
        self.browser = driver
        self.browser.maximize_window()

    def find_filds(self): #находим поля снова
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.address = (By.ID, "address")
        self.zip_code = (By.ID, "zip-code")
        self.city = (By.ID, "city")
        self.country = (By.ID, "country")
        self.email = (By.ID, "e-mail")
        self.phone = (By.ID, "phone")
        self.job_position = (By.ID, "job-position")
        self.company = (By.ID, "company")
        
    def get_properties_first_name(self): #получаем значение класса, чтобы знать каким цветом подсвечены
        return self.browser.find_element(*self.first_name).get_attribute("class")
    
    def get_properties_last_name(self):
        return self.browser.find_element(*self.last_name).get_attribute("class")
    
    def get_properties_address(self):
        return self.browser.find_element(*self.address).get_attribute("class")
    
    def get_properties_zip_code(self):
        return self.browser.find_element(*self.zip_code).get_attribute("class")
    
    def get_properties_city(self):
        return self.browser.find_element(*self.city).get_attribute("class")
    
    def get_properties_country(self):
        return self.browser.find_element(*self.country).get_attribute("class")
    
    def get_properties_email(self):
        return self.browser.find_element(*self.email).get_attribute("class")
    
    def get_properties_phone(self):
        return self.browser.find_element(*self.phone).get_attribute("class")
    
    def get_properties_job_position(self):
        return self.browser.find_element(*self.job_position).get_attribute("class")
    
    def get_properties_job_company(self):
        return self.browser.find_element(*self.company).get_attribute("class")
    