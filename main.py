import account
import settings

import browsers.chrome as chrome
import browsers.firefox as firefox

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def get_browser_driver():
    browser = settings.get_browser()

    if browser == "chrome":
        return chrome.get_driver()
    elif browser == "firefox":
        return firefox.get_driver()
    else:
        raise Exception("Unknown browser!")

def login(driver, email, passwd):
    email_element = (By.XPATH, '//input[@type="email" and @name="loginfmt"]')
    passwd_element = (By.XPATH, '//input[@type="password" and @name="passwd"]')
    next_element = (By.XPATH, '//input[@type="submit" and @id="idSIButton9"]')

    enter = ActionChains(driver)
    shift_tab = ActionChains(driver)

    enter.send_keys(Keys.ENTER)
    shift_tab.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(email_element)).send_keys(email)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(next_element)).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(passwd_element)).send_keys(passwd)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(next_element)).click()
    shift_tab.perform()
    enter.perform()

def pick_menu(driver, menu):
    driver.find_element(By.XPATH, f'//input[@type="checkbox" and @id="AvailablePackets_{menu}__Selected"]').click()
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

def order_lunch(driver):
    while(True):
        try:
            button = driver.find_element(By.XPATH, '//tr[./td[@class="alert-danger"]]/td/a[@class="btn btn-primary"]')
        except NoSuchElementException:
            break
        
        button.click()
        pick_menu(driver, 0)

def main():
    URL = "https://menu.codingburgas.bg"
    driver = get_browser_driver()

    driver.get(URL)

    login_button = driver.find_element(By.XPATH, '//button[text()="Office 365"]')
    login_button.click()

    acc = account.get_account()
    email = acc["user"]
    passwd = acc["password"]

    login(driver, email, passwd)

    order_lunch(driver)

    driver.quit()

if __name__ == "__main__":
    main()