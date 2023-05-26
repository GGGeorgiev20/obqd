import default
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

def default_to_dict(menu, selection):
    hashtable = hashtable_template.copy()
    hashtable["main"] = menu[1]
    hashtable["dessert"] = menu[2]

    if hashtable["main"] == "Кюфте / кебапче с топла гарнитура - 3 бр.":
        hashtable.pop("main")
        menu_settings["grill"] = 3
        menu_settings["main"] = 0

    for key, value in hashtable.items():
        hashtable[key] = selection.index(value)

    return hashtable

def get_selections(dict):
    selections = []

    for key, value in menu_settings.items():
        if value != 0:
            selections.append((dict[key], value))

    return selections

def setup(m_driver, settings):
    global driver
    driver = m_driver

    global menu_settings
    menu_settings = settings

def select_items():
    menus = default.get_menus()
    dish = default.compare_dishes(menus[0][1],menus[1][1])
    menu = menus[0][0], dish, menus[0][2]

    print(menu)

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

    mydict = default_to_dict(menu, food_selection)
    print(mydict)
    
    order_info = get_selections(mydict)
    print(order_info)

    for index, quantity in order_info: 
        checkboxes[index].click()
        count_of_items[index].send_keys(Keys.DELETE)
        count_of_items[index].send_keys(quantity)

    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    print("Order placed")
