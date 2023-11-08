import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
command = """SELECT *
FROM table_name"""
rows = cursor.execute(command).fetchall()
for row in rows:
    print(row)
connection.close()