import os
import json

ACCOUNT_FOLDER = "settings"
ACCOUNT_FILE = "account.json"
ACCOUNT_PATH = os.path.join(ACCOUNT_FOLDER, ACCOUNT_FILE)

def get_account():
    with open(ACCOUNT_PATH, 'r') as f:
        account = json.load(f)
    
    account["user"] = f'{account["user"]}@codingburgas.bg'
    return account