import os

from selenium.webdriver.common.by import By

hashtable = {
    "tarator": "Таратор",
    "salad": "Салата от пресни зеленчуци",
    "main": "",
    "grill": "Кюфте / кебапче",
    "dessert": "",
    "bread": "Филия хляб"
}

def default_to_dict(default, selection):
    hashtable["main"] = default[1]
    hashtable["dessert"] = default[2]

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

def main():
    default = [ "Таратор", "Мусака", "Плод" ]
    selection = [ "Таратор", "Огретен Тиквички", "Мусака", "Салата от пресни зеленчуци", "Кюфте / кебапче", "Плод", "Филия хляб", "Доматена крем супа" ]
    settings = {
        "tarator": 1,
        "salad": 0,
        "main": 1,
        "grill": 0,
        "dessert": 1,
        "bread": 2
    }

    setup(None, settings)

    mydict = default_to_dict(default, selection)

    print(get_selections(mydict))

    # (0, 1) - 1 number of items from index 0
    # so 1 musaka
    # (6, 2) - 2 number of items from index 6
    # so 2 breads
    # returns an array of tuples

if __name__ == "__main__":
    main()