from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    for click in range(5):
        add_button = chrome.find_element(By.CSS_SELECTOR,'[onclick="addElement()"]').click()
        add_button = firefox.find_element(By.CSS_SELECTOR,'[onclick="addElement()"]').click()
        
        sleep(1)

        chrome_delete_buttons = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
        firefox_delete_buttons = firefox.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')

    print(
        f"размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")
except Exception as ex:
    print(ex)    
finally:
    chrome.quit()
    firefox.quit()
