#!/usr/bin/python3
"""Module"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    for state in cursor.fetchall():
        print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()
