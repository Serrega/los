from getpass import getpass
import pickle
import requests


def check_cookies(url: str) -> str:
    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass('enter PHPSESSID cookie: ')}
        save_cookies(cook)

    if "location.href='../';" in (requests.get(url, cookies=cook)).text:
        print('You need to login in browser or input new cookie.')
        exit(1)
        
    return cook


def save_cookies(cooks: dict):
    try:
        with open('cooks.pickle', 'wb') as f:
            pickle.dump(cooks, f)
    except:
        print('can not write cookies')
        exit(1)