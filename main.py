import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--incognito")

chromedriver_path = "./chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

url = "https://menu.codingburgas.bg"
driver.get(url)

login_button = driver.find_element(By.XPATH, '//button[text()="Office 365"]')
login_button.click()

email = ""
passwd = ""

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

time.sleep(5)
driver.quit()