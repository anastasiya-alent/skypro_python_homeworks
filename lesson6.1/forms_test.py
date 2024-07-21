from selenium.webdriver.common.by import By


def test_from(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    search_input_f = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    search_input_f.send_keys("Иван")

    search_input_l = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    search_input_l.send_keys("Петров")

    search_input_add = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    search_input_add.send_keys("Ленина, 55-3")

    search_input_zip = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
    search_input_zip.send_keys("")

    search_input_сity = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    search_input_сity.send_keys("Москва")

    search_input_cou = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    search_input_cou.send_keys("Россия")

    search_input_m = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    search_input_m.send_keys("test@skypro.com")

    search_input_p = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    search_input_p.send_keys("+7985899998787")

    search_input_j = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    search_input_j.send_keys("QA")

    search_input_comp = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    search_input_comp.send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "company").get_attribute("class")
