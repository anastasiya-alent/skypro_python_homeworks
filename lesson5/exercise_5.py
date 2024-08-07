from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("https://the-internet.herokuapp.com/inputs")
    firefox.get("https://the-internet.herokuapp.com/inputs")

    input_field_c = chrome.find_element(By.CSS_SELECTOR, '[type="number"]')
    input_field_c.send_keys("1000")
    sleep(2)

    input_field_c.clear()
    sleep(1)

    input_field_c.send_keys("999")
    sleep(2)

    input_field_f = firefox.find_element(By.CSS_SELECTOR, '[type="number"]')
    input_field_f.send_keys("1000")
    sleep(2)

    input_field_f.clear()
    sleep(1)

    input_field_f.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
