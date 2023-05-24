import os
import json

import default
import selection

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

SETTINGS_FOLDER = 'settings'

MENU_FILE = 'menu.json'
MENU_PATH = os.path.join(SETTINGS_FOLDER, MENU_FILE)

DAYS = {
    "Понеделник": "Monday",
    "Вторник": "Tuesday",
    "Сряда": "Wednesday",
    "Четвъртък": "Thursday",
    "Петък": "Friday"
}

def get_day(day):
    return DAYS[day]

def get_menu_settings():
    global menu_settings
    
    with open(MENU_PATH, 'r') as f:
        menu_settings = json.load(f)
    
    menu_settings = [ menu_settings[key] for key in menu_settings ]

def should_order_menu():
    default_menu = [ 1, 0, 1, 1, 2 ]

    return menu_settings == default_menu

def order_menu():
    menus = default.get_menus()

    pick = default.pick_menu(menus[0], menus[1])

    default.select_menu(pick)

    return pick

def order_lunch(m_driver):
    global driver
    driver = m_driver

    current = 0
    number_of_buttons = 0

    default.setup(driver)
    selection.setup(driver, menu_settings)

    get_menu_settings()

    while(True):
        try:
            buttons = driver.find_elements(By.XPATH, '//tr[./td[@class="alert-danger"]]/td/a[@class="btn btn-primary"]')
        except NoSuchElementException:
            break

        if number_of_buttons == len(buttons):
            current += 1 
        number_of_buttons = len(buttons)

        day = driver.find_elements(By.XPATH, '//tr[./td/@class="alert-danger"]/td[1]')

        try:
            date = day[current].text.split('\n')[0]
            day = get_day(day[current].text.split('\n')[1])

            buttons[current].click()
        except IndexError:
            break

        if should_order_menu():
            pick = order_menu()

            if pick == -1:
                print(f"INFO: No menu for {day} ({date})")
            else:
                print(f"INFO: Selected menu {pick + 1} for {day} ({date})")
        else:
            # todo: svobodna konsumaciq
            pass
