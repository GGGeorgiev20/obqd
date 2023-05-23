import os
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

SETTINGS_FOLDER = 'settings'

PREFERENCES_FILE = 'preferences.txt'
PREFERENCES_PATH = os.path.join(SETTINGS_FOLDER, PREFERENCES_FILE)

MENU_FILE = 'menu.json'
MENU_PATH = os.path.join(SETTINGS_FOLDER, MENU_FILE)

def get_preferences():
    global preferences

    with open(PREFERENCES_PATH, encoding="utf-8", mode='r') as f:
      preferences = f.read().splitlines()
    print(preferences)

def compare_dishes(dish1, dish2):
    index1 = preferences.index(dish1)
    index2 = preferences.index(dish2)

    if index1 < index2:
        return 0
    return 1

def get_menu(menu):
    return driver.find_element(By.XPATH, f'//label[@for="AvailablePackets_{menu}__Selected"]').text.split("\n4.")[0].split("\n")

def get_pick(menu1, menu2):
    print(menu1)
    print(menu2)
    return compare_dishes(menu1[1][3:], menu2[1][3:])

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

        pick = get_pick(get_menu(0),get_menu(1))
        print(pick)
        select_menu(pick)
