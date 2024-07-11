from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")

    locator = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"

    for click in range(3):

        blue_button_c = chrome.find_element(By.XPATH, locator).click()
        # кликаем на ОК в модальном окне
        sleep(1)

        chrome.switch_to.alert.accept()
        sleep(1)

        blue_button_f = firefox.find_element(By.XPATH, locator).click()
        # кликаем на ОК в модальном окне
        sleep(1)

        firefox.switch_to.alert.accept()
        sleep(1)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
