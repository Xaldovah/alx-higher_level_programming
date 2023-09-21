#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to a MySQL database and retrieves data from the 'cities'
    and 'states' tables.
    Joins the tables to display city names of the specified state.

    Command-line arguments:
    - argv[1]: MySQL username
    - argv[2]: MySQL password
    - argv[3]: MySQL database name
    - argv[4]: State name

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
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC""", (argv[4],))

        rows = cur.fetchall()

    if rows:
        city_names = [row[0] for row in rows]
        print(", ".join(city_names))
    else:
        print()
