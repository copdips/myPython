import sqlite3

import requests

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()
cursor


from copy import deepcopy


def dict_of_dicts_merge(x, y):
    if not (isinstance(x, dict) and isinstance(y, dict)):
        return y
    z = {}
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = dict_of_dicts_merge(x[key], y[key])
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    return z


print("hello")
