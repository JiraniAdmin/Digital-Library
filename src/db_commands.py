#!/usr/bin/python
import sqlite3


def add_book(title, author, path, description):
    # Add a new book
    # Connect to SQLite database
    conn = sqlite3.connect('/home/jirani/library.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO books (title, author, path, description) VALUES (?, ?, ?, ?)', (title, author, path, description))
    
    # Retrieve the new count
    # cursor.execute('SELECT book_count FROM counters WHERE id = 1')
    # count = cursor.fetchone()[0]
    print(f"Book {title} added.")

    conn.close()

try:
        # Check if database already exists    
        db_path = f"/home/jirani/{database}"

        if os.path.exists(db_path)
            print(f"Database '{database}' already exists.")
            return False

        # Connect to SQLite database and create cursor to interact with db 
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create a table with columns "title", "author", "path", and "description"
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            path TEXT,
            description TEXT
        )
        ''')

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

        print("Database table created with columns: title, author, path, description")
        return True

add_book("Lorax", "Dr. Suess", "/home/jirani", "Children's Book")

