# This is file contains all the needed functions to work with mysql

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        #user="db_user",
        #password="db_user_passwd",
        #host="192.0.2.1",
        #port=3306,
        database="app"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("select * from parking;")
for i in cur:
    print (i)


def string_parser():
