#!/usr/bin/python3
"""Creates a script that adds all arguments to a Python list,
then saves them to a file"""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

a_list = []

try:
    a_list = load_from_json_file("add_item.json")
    save_to_json_file(a_list + sys.argv[1:], "add_item.json")
except:
    save_to_json_file(a_list + sys.argv[1:], "add_item.json")
