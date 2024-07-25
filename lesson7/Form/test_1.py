from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from FirstPage import FirstPage
from SecondPage import SecondPage

def test_assertion():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    first_page = FirstPage(browser)
    first_page.find_filds()
    first_page.send_keys()
    first_page.click_Submit()

    second_page = SecondPage(browser)
    second_page.find_filds()
    second_page.get_properties_first_name()
    second_page.get_properties_last_name()
    second_page.get_properties_address()
    second_page.get_properties_zip_code()
    second_page.get_properties_city()
    second_page.get_properties_country()
    second_page.get_properties_email()
    second_page.get_properties_phone()
    second_page.get_properties_job_position()
    second_page.get_properties_job_company()
       
    assert "success" in second_page.get_properties_first_name()
    assert "success" in second_page.get_properties_last_name()
    assert "success" in second_page.get_properties_address()
    assert "danger" in second_page.get_properties_zip_code()
    assert "success" in second_page.get_properties_city()
    assert "success" in second_page.get_properties_country()
    assert "success" in second_page.get_properties_email()
    assert "success" in second_page.get_properties_phone()
    assert "success" in second_page.get_properties_job_position()
    assert "success" in second_page.get_properties_job_company()
       