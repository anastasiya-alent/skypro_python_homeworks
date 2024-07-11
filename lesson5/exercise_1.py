from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    locator = '[onclick="addElement()"]'
    del_locator = '[onclick="deleteElement()"]'

    for click in range(5):
        chrome.find_element(By.CSS_SELECTOR, locator).click()
        firefox.find_element(By.CSS_SELECTOR, locator).click()
        sleep(1)

        ch_del_buttons = chrome.find_elements(By.CSS_SELECTOR, del_locator)
        ff_del_buttons = firefox.find_elements(By.CSS_SELECTOR, del_locator)

    print(
        f"размер списка кнопок Delete в Chrome: {len(ch_del_buttons)}")
    print(
        f"размер списка кнопок Delete в Firefox: {len(ff_del_buttons)}")

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
