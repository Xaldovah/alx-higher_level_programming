#!/usr/bin/python3
"""import modules"""

from os import path
from sys import argv

"""adds all arguments to a Python list, and then save them to a file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""check if path exists"""
if path.exists('add_item.json'):
    json_obj = load_from_json_file('add_item.json')
else:
    json_obj = []

for i in range(1, len(argv)):
    json_obj.append(argv[i])

save_to_json_file(json_obj, 'add_item.json')
