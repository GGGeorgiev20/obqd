import os
import json
import getpass

ACCOUNT_FOLDER = "settings"
ACCOUNT_FILE = "account.json"
ACCOUNT_PATH = os.path.join(ACCOUNT_FOLDER, ACCOUNT_FILE)

def create_account():
    print("INFO: No account found")
    print("INFO: Creating account\n")

    account = {}
    account["user"] = input("User: ")
    account["password"] = getpass.getpass("Password: ")
    
    print("\nINFO: Account created successfully\n")
    
    with open(ACCOUNT_PATH, 'w') as f:
        json.dump(account, f, indent=4)

def get_account():
    if not os.path.exists(ACCOUNT_PATH):
        create_account()

    with open(ACCOUNT_PATH, 'r') as f:
        account = json.load(f)
    
    if not account["user"] or not account["password"]:
        create_account()
        return get_account()
    
    account["user"] = f'{account["user"]}@codingburgas.bg'
    return account