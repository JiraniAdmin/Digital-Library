import sqlite3

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect("books.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table with columns "title" and "author"
cursor.execute('''CREATE TABLE books
                  (title TEXT, author TEXT)'')

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("SQLite database 'books.db' with 'title' and 'author' columns created.")
