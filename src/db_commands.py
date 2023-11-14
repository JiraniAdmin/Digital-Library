import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS counters (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    book_count INTEGER DEFAULT 0
)
''')

# Initialize counter
cursor.execute('INSERT OR IGNORE INTO counters (id, book_count) VALUES (1, 0)')
conn.commit()

def add_book(title, author):
    # Add a new book
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    
    # Increment the counter
    cursor.execute('UPDATE counters SET book_count = book_count + 1 WHERE id = 1')
    conn.commit()

    # Retrieve the new count
    cursor.execute('SELECT book_count FROM counters WHERE id = 1')
    count = cursor.fetchone()[0]
    print(f"Book added. Total books in database: {count}")

# Example usage
add_book("1984", "George Orwell")
add_book("To Kill a Mockingbird", "Harper Lee")

# Close the connection
conn.close()
