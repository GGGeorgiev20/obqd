from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    firefox_options = Options()
    firefox_options.add_argument("--private")
    
    geckodriver_path = "./drivers/geckodriver"

    driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)
    return driver