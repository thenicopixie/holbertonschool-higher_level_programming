#!/usr/bin/python3
"""send search request to Star Wars API using command line argument"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    result = r.json()
    print("Number of results: {}".format(result.get('count')))
    for find in result.get('results'):
            print(find.get('name'))
