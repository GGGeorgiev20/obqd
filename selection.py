import default
from selenium.webdriver.common.by import By

hashtable = {
    "tarator": "Таратор",
    "salad": "Салата от пресни зеленчуци",
    "main": "",
    "grill": "Кюфте / кебапче",
    "dessert": "",
    "bread": "Филия хляб"
}

def default_to_dict(menu, selection):
    hashtable["main"] = menu[1]
    hashtable["dessert"] = menu[2]

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

    selection = [ "Таратор", "Огретен тиквички", "Мусака", "Салата от пресни зеленчуци", "Кюфте / кебапче", "Плод", "Филия хляб", "Доматена крем супа" ]

    mydict = default_to_dict(menu, selection)

    print(get_selections(mydict))

    # (0, 1) - 1 number of items from index 0
    # so 1 musaka
    # (6, 2) - 2 number of items from index 6
    # so 2 breads
    # returns an array of tuples
