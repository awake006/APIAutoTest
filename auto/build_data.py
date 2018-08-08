import random
import string
import time
import sys
from auto.log import console_logger
from auto import global_data


def set_str(n, index):
    '''
    Randomly generate n-bit str
    '''
    try:
        n = int(n)
        source = list(string.ascii_letters) + list(string.digits)
        name = ''
        for _ in range(n):
            name += random.choice(source)
        return name
    except TypeError as e:
        message_error_set_str = 'The use case [%s] parameter setting is incorrect, please check the parameter file [%s]' % (
            index, e)
        console_logger.error(message_error_set_str)
        sys.exit()


def set_time():
    '''strftime'''
    now_time = time.strftime("%Y%m%d%H%M%s", time.localtime())
    return now_time


def get_case_id():
    testcase_id = [i for i in global_data.testcase.keys() if i != '']
    return testcase_id


def get_case_data(testcase_id):
    name = global_data.testcase[testcase_id].get("name")
    function_name = global_data.testcase[testcase_id].get('function')
    method = global_data.testcase[testcase_id].get("method", "GET").upper()
    message = global_data.testcase[testcase_id].get('message', 'success')
    request_type = global_data.testcase[testcase_id].get("type")
    chenk_method = global_data.testcase[testcase_id].get('chenk_method', 'message').upper()
    url = global_data.testcase[testcase_id].get('url')
    return name, function_name, method, message, request_type, chenk_method, url