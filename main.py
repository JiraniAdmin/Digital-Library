import sqlite3

def connect_to_db(db_file):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_file)
    return conn

def search_books(conn, title=None, author=None):
    """Search for books by title or author."""
    cur = conn.cursor()
    
    if title:
        cur.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    elif author:
        cur.execute("SELECT books.* FROM books JOIN authors ON books.author_id = authors.id WHERE authors.name LIKE ?", ('%' + author + '%',))
    else:
        print("Please provide a book title or author's name.")
        return

    books = cur.fetchall()
    for book in books:
        print(book)

def main():
    database = "your_database.db"  # Replace with your SQLite database file
    
    # Connect to the database
    conn = connect_to_db(database)

    # Example search
    search_input = input("Enter a book title or author's name: ")
    if " " in search_input:  # Assuming author names have spaces and titles may not
        search_books(conn, author=search_input)
    else:
        search_books(conn, title=search_input)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
