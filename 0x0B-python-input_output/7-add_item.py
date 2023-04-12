#!/usr/bin/python3
""" Adds all arguments to a Python list and saves them to a file """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv[1:]

try:
    args_list_in_file = load_from_json_file("add_item.json")
except FileNotFoundError:
    args_list_in_file = []

args_list_in_file.extend(args)

save_to_json_file(args_list_in_file, "add_item.json")
