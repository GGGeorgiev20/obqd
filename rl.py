from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def remove_lunch(driver):
    while(True):
        try:
            button = driver.find_element(By.XPATH, '//tr[./td[@class="alert-success"]]/td/a[@class="btn btn-danger"]')
        except NoSuchElementException:
            break

        button.click()
        driver.find_element(By.XPATH, '//input[@type="submit" and @value="Анулирай"]').click()

        print("INFO: Removed lunch")
        