from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")
    locator = '//button[@class="btn btn-primary"]'

    for click in range(3):
        blue_button_c = chrome.find_element(By.XPATH, locator).click()
        blue_button_f = firefox.find_element(By.XPATH, locator).click()
        count = count + 1
        sleep(1)

    print(count)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
