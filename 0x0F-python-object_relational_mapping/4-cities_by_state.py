#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to a MySQL database and retrieves data
    from the 'cities' and 'states' tables.
    Joins the tables to display city names along with
    their respective state names.

    Command-line arguments:
    - argv[1]: MySQL username
    - argv[2]: MySQL password
    - argv[3]: MySQL database name

    Prints the retrieved data to the console.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    with db.cursor() as cur:
        cur.execute("""
            SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)

    cur.close()
    db.close()
