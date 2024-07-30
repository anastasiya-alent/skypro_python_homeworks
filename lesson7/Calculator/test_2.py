from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPageCal

def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPageCal(browser)
    main_page.input_time()
    main_page.entering_values_click()
    assert "15" in main_page.checking_value()


