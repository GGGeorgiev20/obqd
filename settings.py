import os
import json

SETTINGS_FOLDER = 'settings'
SETTINGS_FILE = 'settings.json'
SETTINGS_PATH = os.path.join(SETTINGS_FOLDER, SETTINGS_FILE)

def get_settings():
    with open(SETTINGS_PATH, 'r') as f:
        settings = json.load(f)
        
    return settings

def get_browser():
    settings = get_settings()
    return settings['browser']

def get_grill_backup():
    settings = get_settings()
    return settings['grill_backup']