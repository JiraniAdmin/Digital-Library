#!/usr/bin/python
import pprint
from datetime import datetime, timedelta
import os
import sys
import sqlite3


def add_book(title, author, path, description):
    """
    This function adds a new book to the database table

    Args:
        title (string): Title of the book
        author (string): Author of the book
        path (string): Path where the book is saved
        description (string): Short description of book

    Return:
        bool: True if book was added, otherwise false
    """
    try:
        # Add a new book
        # Connect to SQLite database
        conn = sqlite3.connect('/home/jirani/library.db')
        cursor = conn.cursor()

        # Check if book already exists

        cursor.execute('''
            INSERT INTO books 
            (title, author, path, description) 
            VALUES (?, ?, ?, ?)''', 
            (title, author, path, description))

        
        # Check for the book again to make sure it is there

        print(f"{title} added to the database.")

        conn.close()

    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
        return False
        
    except Exception as err:
        print(f"Error occurred: {err}")
        return False


add_book("Lorax", "Dr. Suess", "/home/jirani", "Children's Book")
