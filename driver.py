import os
import sys
import zipfile
import requests

import settings

DRIVERS_FOLDER = "drivers"

DRIVERS = {
    "chrome": {
        "driver": "chromedriver.zip",
        "url": "https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_win32.zip"
    },
    "firefox": {
        "driver": "geckodriver.zip",
        "url": "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win32.zip"
    }
}

def should_download_driver(browser):
    driver_path = os.path.join(DRIVERS_FOLDER, DRIVERS[browser]['driver'])

    return not os.path.exists(driver_path)

def download_driver(driver_url, save_path):
    response = requests.get(driver_url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("INFO: Driver downloaded successfully")
    else:
        print("ERROR: Driver download failed")
        sys.exit(1)

def extract_driver(zip_path, extract_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

def setup():
    browser = settings.get_browser()

    if not should_download_driver(browser):
        return
    
    print("INFO: No driver found")
    
    if not os.path.exists(DRIVERS_FOLDER):
        os.makedirs(DRIVERS_FOLDER)
    
    driver_url = DRIVERS[browser]['url']

    driver_path = os.path.join(DRIVERS_FOLDER, DRIVERS[browser]['driver'])

    download_driver(driver_url, driver_path)

    extract_driver(driver_path, DRIVERS_FOLDER)

    os.remove(driver_path)

if __name__ == "__main__":
    setup()