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
    preferences = [line for line in preferences if not line.endswith("X")]
    print(preferences)

def get_menu_settings():
    global settings
    
    with open(MENU_PATH, 'r') as f:
        settings = json.load(f)

def index_dish(dish):
    try:
        index = preferences.index(dish)
    except ValueError:
        index = -1
    return index

def compare_dishes(dish1, dish2):
    index1 = index_dish(dish1)
    index2 = index_dish(dish2)
    
    if index1 == index2:
        return ""
    if index1 < 0 and index2 >= 0:
        return dish2 
    elif index1 >= 0 and index2 < 0:
        return dish1

    if index1 < index2:
        return dish1
    return dish2

def pick_menu(menu1, menu2):
    menu = compare_dishes(menu1[1], menu2[1]) 
    if menu == "": return -1
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
    return (settings["tarator"] == 1
    and settings["salad"] == 0
    and settings["main"] == 1
    and settings["dessert"] == 1
    and settings["bread"] == 2)

def order_lunch(m_driver):
    global driver
    driver = m_driver

    get_preferences()
    get_menu_settings()

    cur_button = 0
    num_of_buttons = 0

    while(True):
        try:
            buttons = driver.find_elements(By.XPATH, '//tr[./td[@class="alert-danger"]]/td/a[@class="btn btn-primary"]')
        except NoSuchElementException:
            break
        if num_of_buttons == len(buttons):
            cur_button += 1 
        num_of_buttons = len(buttons)
        
        try:
            buttons[cur_button].click()
        except IndexError:
            break

        if order_menu():
            menus = get_menus()

            pick = pick_menu(menus[0], menus[1])

            select_menu(pick)

            print(f"INFO: Selected menu {pick + 1}")
        else:
            print("Free consumption shit")
