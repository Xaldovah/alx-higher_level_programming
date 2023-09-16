#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to a MySQL database and retrieves data from the 'states' table.

    Command-line arguments:
    - argv[1]: MySQL username
    - argv[2]: MySQL password
    - argv[3]: MySQL database name

    Prints the retrieved data to the console.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT * FROM states WHERE name LIKE BINARY %(name)s
            ORDER BY states.id ASC""", {'name': argv[4]})
        rows = cur.fetchall()
    if rows is not NONE:
        for row in rows:
            print(row)
    cur.close()
    conn.close()
