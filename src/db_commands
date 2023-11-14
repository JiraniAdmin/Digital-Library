import sqlite3

def create_library_database():
    # Connect to SQLite database (or create a new one if it doesn't exist)
    db_path = "home/jirani/library.db"
    conn = sqlite3.connect(db_path)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table with columns "Title", "Author", "Path", and "Description"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            Title TEXT,
            Author TEXT,
            Path TEXT,
            Description TEXT
        )
    ''')

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

       print("'Author', 'Path', and 'Description' columns created.")

if __name__ == "__main__":
    create_library_database()

create_library_database()

          
