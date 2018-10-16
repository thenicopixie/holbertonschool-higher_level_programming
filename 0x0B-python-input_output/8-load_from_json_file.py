#!/usr/bin/python3
"""Makes a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        return json.load(a_file)
