#!/usr/bin/python3
"""fetch URL module using command line argument"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    html = dict(response.info())

print(html.get("X-Request-Id"))
