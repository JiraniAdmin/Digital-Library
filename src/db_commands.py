import sqlite3


def add_book(title, author):
    # Add a new book
    # Connect to SQLite database
    conn = sqlite3.connect('/home/jirani/library.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    
    # Retrieve the new count
    # cursor.execute('SELECT book_count FROM counters WHERE id = 1')
    # count = cursor.fetchone()[0]
    print(f"Book {title} added.")

    conn.close()

# Example usage
add_book("1984", "George Orwell")
add_book("To Kill a Mockingbird", "Harper Lee")

# Close the connection
conn.close()
