#!/usr/bin/python3
"""Script that lists all states with a name starting with N
safe from injections"""
import MySQLdb
import sys
conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT id, name FROM cities ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
