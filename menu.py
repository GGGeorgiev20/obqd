import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

SETTINGS_FOLDER = 'settings'

PREFERENCES_FILE = 'preferences.txt'
PREFERENCES_PATH = os.path.join(SETTINGS_FOLDER, PREFERENCES_FILE)

MENU_FILE = 'menu.json'
MENU_PATH = os.path.join(SETTINGS_FOLDER, MENU_FILE)

def get_preferences():
    global preferences

    with open(PREFERENCES_PATH, 'r') as f:
      preferences = f.read().splitlines()

def compare_dishes(dish1, dish2):
    index1 = preferences.index(dish1)
    index2 = preferences.index(dish2)

    if index1 < index2:
        return dish1
    return dish2

def get_menus():
    pass

def get_pick(menus):
    pass

def select_menu(menu):
    driver.find_element(By.XPATH, f'//input[@type="checkbox" and @id="AvailablePackets_{menu}__Selected"]').click()
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

def order_lunch(m_driver):
    global driver
    driver = m_driver

    get_preferences()

    while(True):
        try:
            button = driver.find_element(By.XPATH, '//tr[./td[@class="alert-danger"]]/td/a[@class="btn btn-primary"]')
        except NoSuchElementException:
            break
        
        button.click()

        menus = get_menus()
        pick = get_pick(menus)

        select_menu(pick)