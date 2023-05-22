from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chromedriver_path = "./chromedriver"

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    return driver