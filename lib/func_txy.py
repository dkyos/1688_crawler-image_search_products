# !/usr/bin/python
# -*- coding: utf-8 -*-


import random
import string
import requests
import contextlib


def request_post(url, data=None, files={}, headers={}):
    try:
        with contextlib.closing(requests.post(url=url, data=data, files=files, headers=headers)) as req:
            res = req.text
            return "succ", res
    except Exception as e:
        print(e)
        return "fail", {}


def request_get(url, params, headers):
    try:
        with contextlib.closing(requests.get(url=url, params=params, headers=headers)) as req:
            data = req.json()
            return "succ", data
    except Exception as e:
        print(e)
        return "fail", {}


def get_random_str(k):
    return ''.join(random.choices(string.ascii_letters, k=k))
