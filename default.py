import os

from selenium.webdriver.common.by import By

SETTINGS_FOLDER = 'settings'

PREFERENCES_FILE = 'preferences.txt'
PREFERENCES_PATH = os.path.join(SETTINGS_FOLDER, PREFERENCES_FILE)

def get_preferences():
    global preferences

    with open(PREFERENCES_PATH, encoding="utf-8", mode='r') as f:
        preferences = f.read().splitlines()
    
    preferences = [ line for line in preferences if not line.endswith("X") ]

def index_dish(dish):
    try:
        return preferences.index(dish)
    except ValueError:
        return -1

def compare_dishes(dish1, dish2):
    index1 = index_dish(dish1)
    index2 = index_dish(dish2)
    
    if index1 == index2:
        return -1

    if index1 == -1:
        return dish2
    elif index2 == -1:
        return dish1

    if index1 < index2:
        return dish1
    return dish2

def pick_menu(menu1, menu2):
    dish = compare_dishes(menu1[1], menu2[1])

    if dish == -1:
        return -1

    return int(dish == menu2[1])

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

def setup(m_driver):
    global driver
    driver = m_driver

    get_preferences()