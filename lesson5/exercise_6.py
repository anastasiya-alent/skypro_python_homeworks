from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("https://the-internet.herokuapp.com/login")
    firefox.get("https://the-internet.herokuapp.com/login")

    input_name = chrome.find_element(By.CSS_SELECTOR, "#username")
    input_name.send_keys("tomsmith")
    input_password = chrome.find_element(By.CSS_SELECTOR, "#password")
    input_password.send_keys("SuperSecretPassword!")
    sleep(1)
    login_button = chrome.find_element(By.CSS_SELECTOR,'.radius').click()
    sleep(1)
    input_name = firefox.find_element(By.CSS_SELECTOR, "#username")
    input_name.send_keys("tomsmith")
    input_password = firefox.find_element(By.CSS_SELECTOR, "#password")
    input_password.send_keys("SuperSecretPassword!")
    sleep(1)
    login_button = firefox.find_element(By.CSS_SELECTOR,'.radius').click()
    sleep(1)   
except Exception as ex:
    print(ex)  
finally:
    chrome.quit()
    firefox.quit()