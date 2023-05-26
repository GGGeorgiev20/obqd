import default
import settings

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

hashtable_template = {
    "tarator": "Таратор",
    "salad": "Салата от пресни зеленчуци",
    "main": "",
    "grill": "Кюфте / кебапче",
    "dessert": "",
    "bread": "Филия хляб"
}

current_menu_settings = {}

def default_to_dict(menu, selection):
    hashtable = hashtable_template.copy()
    hashtable["main"] = menu[1]
    hashtable["dessert"] = menu[2]

    if hashtable["main"] == "Кюфте / кебапче с топла гарнитура - 3 бр.":
        hashtable.pop("main")
        current_menu_settings["grill"] += 3 * menu_settings["main"]
        current_menu_settings["main"] = 0

    for key, value in hashtable.items():
        hashtable[key] = selection.index(value)

    return hashtable

def get_selections(dict):
    selections = []

    for key, value in current_menu_settings.items():
        if value != 0:
            selections.append((dict[key], value))

    return selections

def setup(m_driver, settings):
    global driver
    driver = m_driver

    global menu_settings
    menu_settings = settings

def select_items():
    global current_menu_settings
    current_menu_settings = menu_settings.copy()

    pick = default.get_pick()
    menu = default.get_menus()[pick]

    checkboxes = []
    food_selection = [] 
    count_of_items = []

    for i in range(0, 8):
        try:
            checkboxes.append(driver.find_element(By.XPATH, f'//input[@id="AvailableItems_{i}__Selected"]'))
            food_selection.append(driver.find_element(By.XPATH, f'//label[@for="AvailableItems_{i}__Selected"]').text)
            count_of_items.append(driver.find_element(By.XPATH, f'//input[@id="AvailableItems_{i}__Quantity"]'))
        except NoSuchElementException:
            break

    menu_dict = default_to_dict(menu, food_selection)

    index_main = -1
    if pick == -1:
        index_main = menu_dict["main"]
        current_menu_settings["grill"] = 3

        if not settings.get_grill_backup():
            return False
    
    order_info = get_selections(menu_dict)

    for index, quantity in order_info:
        if index == index_main:
            continue
        
        checkboxes[index].click()
        count_of_items[index].send_keys(Keys.DELETE)
        count_of_items[index].send_keys(quantity)

    driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    return True
