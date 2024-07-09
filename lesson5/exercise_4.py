from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:

    wait_c = WebDriverWait(chrome, 10)
    chrome.get("https://the-internet.herokuapp.com/entry_ad")
    sleep(2)
    close_button_c = wait_c.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".modal-footer"))).click()
    sleep(2)

    wait_f = WebDriverWait(firefox, 10)
    firefox.get("https://the-internet.herokuapp.com/entry_ad")
    sleep(2)
    close_button_f = wait_f.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".modal-footer"))).click()
    sleep(2)
except Exception as ex:
    print(ex)   
finally:
    chrome.quit()
    firefox.quit()