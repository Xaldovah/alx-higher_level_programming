#!/usr/bin/python3
"""
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
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
    - argv[4]: State name to search for

    Prints the retrieved data to the console.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT * FROM states WHERE name LIKE BINARY %(name)s
            ORDER BY states.id ASC""", {'name': argv[4]})
        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)

    cur.close()
    db.close()
