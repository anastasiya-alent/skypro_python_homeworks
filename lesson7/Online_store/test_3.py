from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.AuthorizationPage import Authorization
from Pages.AddCartPage import AddCart
from Pages.CartPage import Cart
from Pages.FormPage import Form
from Pages.TotalPage import Total


def test_online_store():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    authorization_page = Authorization(browser)
    authorization_page.authorization()
    authorization_page.click_button()

    add_cart_page = AddCart(browser)
    add_cart_page.add_cart()

    cart_page = Cart(browser)
    cart_page.click_checkout()

    form_page = Form(browser)
    form_page.data_input()
    form_page.click_continue()

    total_page = Total(browser)
    total_page.total()
    assert total_page.total == "58.29"




    