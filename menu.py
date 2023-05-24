import os
import json

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

SETTINGS_FOLDER = 'settings'

PREFERENCES_FILE = 'preferences.txt'
PREFERENCES_PATH = os.path.join(SETTINGS_FOLDER, PREFERENCES_FILE)

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

def get_preferences():
    global preferences

    with open(PREFERENCES_PATH, encoding="utf-8", mode='r') as f:
        preferences = f.read().splitlines()
    
    preferences = [ line for line in preferences if not line.endswith("X") ]

def get_menu_settings():
    global menu_settings
    
    with open(MENU_PATH, 'r') as f:
        menu_settings = json.load(f)
    
    menu_settings = [ menu_settings[key] for key in menu_settings ]

def index_dish(dish):
    try:
        return preferences.index(dish)
    except ValueError:
        return False

def compare_dishes(dish1, dish2):
    index1 = index_dish(dish1)
    index2 = index_dish(dish2)
    
    if index1 == index2:
        global skipped
        skipped += 1
        return False

    if not index1:
        return dish2
    elif not index2:
        return dish1

    if index1 < index2:
        return dish1
    return dish2

def pick_menu(menu1, menu2):
    menu = compare_dishes(menu1[1], menu2[1])

    if not menu:
        return -1

    return int(menu == menu2[1])

def get_menus():
    menus = []

    for i in range(2):
        menu = driver.find_element(By.XPATH, f'//label[@for="AvailablePackets_{i}__Selected"]')

        menu = menu.text.split("\n4.")[0].split("\n")
        menu = [ i[3:] for i in menu ]

        menus.append(menu)

    return menus

def select_menu(menu):
    if menu == -1:
        driver.find_element(By.XPATH, '//a[@href="/Reservations"]').click() 
        return

    driver.find_element(By.XPATH, f'//input[@type="checkbox" and @id="AvailablePackets_{menu}__Selected"]').click()
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

def order_menu():
    default_menu = [ 1, 0, 1, 1, 2 ]

    return menu_settings == default_menu

def order_lunch(m_driver):
    global driver
    driver = m_driver

    global skipped
    skipped = 0

    get_preferences()
    get_menu_settings()

    while(True):
        try:
            buttons = driver.find_elements(By.XPATH, '//tr[./td[@class="alert-danger"]]/td/a[@class="btn btn-primary"]')
        except NoSuchElementException:
            break

        if skipped >= len(buttons):
            break

        day = driver.find_elements(By.XPATH, '//tr[./td/@class="alert-danger"]/td[1]')

        date = day[skipped].text.split('\n')[0]
        day = get_day(day[skipped].text.split('\n')[1])

        buttons[skipped].click()

        if order_menu():
            menus = get_menus()

            pick = pick_menu(menus[0], menus[1])

            select_menu(pick)

            if pick == -1:
                print(f"INFO: No menu for {day} ({date})")
            else:
                print(f"INFO: Selected menu {pick + 1} for {day} ({date})")
        else:
            # todo: svobodna konsumaciq
            pass
