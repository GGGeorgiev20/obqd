from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chromedriver_path = "../drivers/chromedriver.exe"
    service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
