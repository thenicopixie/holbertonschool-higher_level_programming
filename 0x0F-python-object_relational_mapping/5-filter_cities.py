#!/usr/bin/python3
"""Script that lists all cities of a state from a database"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cmd = """SELECT cities.name FROM cities JOIN states ON
          cities.state_id = states.id WHERE states.name = %s"""
    cur.execute(cmd, (sys.argv[4], ))
    query_rows = cur.fetchall()
    count = 0
    for row in query_rows:
        for col in row:
            if count != len(query_rows) - 1:
                print("{}, ".format(col), end="")
            else:
                print("{}".format(col))
            count += 1
    cur.close()
    conn.close()
