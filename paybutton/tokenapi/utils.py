import requests
import json


def request_url(usr, pwd, device_data):
    headers = {'Accept': 'application/json'}
    url = 'https://paymiumm.pythonanywhere.com/merchant/paymiumm/v1/login'
    return requests.post(url, headers=headers, json= {'usr': usr, 'pwd': pwd,
    'device_data': device_data})