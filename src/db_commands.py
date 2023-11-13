#!/usr/bin/python

# Imports: Standard Libraries
# ---------------------------
import pprint
from datetime import datetime, timedelta
import os
import sys
# import our database once it has been created
import sqlite3

def delete_row_by_book_title(db_path, table_name, book_title):
    """
    This function deletes a book from the database table.

    Args:
        db_path (string): The full path to the database location
        table_name (string): The database table name where the book is located
        book_title (string): The book title which we want to delete
        
    Returns:
        bool: If the book is deleted then return True; otherwise false
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get the author's name
        cursor.execute(f"SELECT author_name FROM {table_name} WHERE book_title = ?", (book_title,))
        result = cursor.fetchone()

        if result is None:
            print(f"{book_title} does not exist in Database")
            return False

        # Execute the SQL DELETE statement to remove the row with the specified book_title
        cursor.execute(f"DELETE FROM {table_name} WHERE title = ?", (book_title,))
        deletion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()

        print(f"Deleted {book_title} at {deletion_time}")
        
    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
        
    except Exception as err:
        print(f"Error occurred: {err}")

# Example usage:
db_path = 'library.db'
table_name = 'your_table_name'
book_title = 'Signs Preceding the End of the World'

delete_row_by_book_title(db_path, table_name, book_title)
