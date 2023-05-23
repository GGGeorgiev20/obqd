import account
import settings
import driver
import menu

import browsers.chrome as chrome
import browsers.firefox as firefox

from selenium.webdriver.support.wait import WebDriverWait
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

def login(m_driver, email, passwd):
    email_element = (By.XPATH, '//input[@type="email" and @name="loginfmt"]')
    passwd_element = (By.XPATH, '//input[@type="password" and @name="passwd"]')
    next_element = (By.XPATH, '//input[@type="submit" and @id="idSIButton9"]')

    enter = ActionChains(m_driver)
    shift_tab = ActionChains(m_driver)

    enter.send_keys(Keys.ENTER)
    shift_tab.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

    WebDriverWait(m_driver, 10).until(EC.element_to_be_clickable(email_element)).send_keys(email)

    WebDriverWait(m_driver, 10).until(EC.element_to_be_clickable(next_element)).click()

    WebDriverWait(m_driver, 10).until(EC.element_to_be_clickable(passwd_element)).send_keys(passwd)

    WebDriverWait(m_driver, 10).until(EC.element_to_be_clickable(next_element)).click()
    shift_tab.perform()
    enter.perform()

def main():
    URL = "https://menu.codingburgas.bg"
    
    acc = account.get_account()
    email = acc["user"]
    passwd = acc["password"]

    driver.setup()

    m_driver = get_browser_driver()

    m_driver.get(URL)

    login_button = m_driver.find_element(By.XPATH, '//button[text()="Office 365"]')
    login_button.click()

    login(m_driver, email, passwd)

    menu.order_lunch(m_driver)

    m_driver.quit()

if __name__ == "__main__":
    main()