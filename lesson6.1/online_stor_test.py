from selenium.webdriver.common.by import By


def test_cart(driver):
    driver.get(" https://www.saucedemo.com/")

    input_name = driver.find_element(By.ID, "user-name")
    input_name.send_keys("standard_user")

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()

    driver.find_element(By.ID, "checkout").click()

    input_n = driver.find_element(By.ID, "first-name")
    input_n.send_keys("Anastasiya")

    input_last = driver.find_element(By.ID, "last-name")
    input_last.send_keys("Alentieva")

    input_code = driver.find_element(By.ID, "postal-code")
    input_code.send_keys("344150")

    driver.find_element(By.ID, "continue").click()

    driver.implicitly_wait(10)

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    total = total.strip().replace("Total: $", "")

    assert total == "58.29"
    print(f"Итоговая сумма равна ${total}")
