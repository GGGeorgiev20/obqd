import os

from selenium.webdriver.common.by import By

def setup(m_driver, settings):
    global driver
    driver = m_driver

    global menu_settings
    menu_settings = settings