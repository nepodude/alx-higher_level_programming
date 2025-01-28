#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC;")

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
