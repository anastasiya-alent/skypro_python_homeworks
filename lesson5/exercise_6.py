from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("https://the-internet.herokuapp.com/login")
    firefox.get("https://the-internet.herokuapp.com/login")

    input_name_c = chrome.find_element(By.CSS_SELECTOR, "#username")
    input_name_c.send_keys("tomsmith")

    input_password_c = chrome.find_element(By.CSS_SELECTOR, "#password")
    input_password_c.send_keys("SuperSecretPassword!")

    sleep(1)

    login_button_c = chrome.find_element(By.CSS_SELECTOR, '.radius').click()

    sleep(1)

    input_name_f = firefox.find_element(By.CSS_SELECTOR, "#username")
    input_name_f.send_keys("tomsmith")

    input_password_f = firefox.find_element(By.CSS_SELECTOR, "#password")
    input_password_f.send_keys("SuperSecretPassword!")

    sleep(1)

    login_button_f = firefox.find_element(By.CSS_SELECTOR, '.radius').click()

    sleep(1)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
