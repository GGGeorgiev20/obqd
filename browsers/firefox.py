from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver():
    firefox_options = Options()
    firefox_options.add_argument("--private")
    
    geckodriver_path = "../drivers/geckodriver.exe"
    service = Service(executable_path=geckodriver_path)

    driver = webdriver.Firefox(service=service, options=firefox_options)
    return driver
