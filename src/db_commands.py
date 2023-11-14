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

add_book("Lorax", "Dr. Suess", "/home/jirani", "Children's Book")

