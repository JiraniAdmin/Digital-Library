#!/usr/bin/python

# Imports: Standard Libraries
# ---------------------------
import pprint
from datetime import datetime, timedelta
import os
import sys
import sqlite3


def create_library_database(database):
    """
    This function creates a new database table with a specified table.

    Args:
         database (string): Name of the database to create
        
    Returns:
        bool: true if database created, otherwise false
    """
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
    
    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
        return False
        
    except Exception as err:
        print(f"Error occurred: {err}")
        return False
