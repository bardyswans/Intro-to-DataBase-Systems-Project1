import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Bradys36!',  
    'database': 'library_db'
}

def connect():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Connection error: {e}")
        return None


def get_all_books():
    conn = connect()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books;")
        result = cursor.fetchall()
        cursor.close()
        return result
    finally:
        conn.close()

def insert_book(title, author, isbn, is_checked_out):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Books (title, author, isbn, is_checked_out)
            VALUES (%s, %s, %s, %s);
        """, (title, author, isbn, is_checked_out))
        conn.commit()
        return True
    except Error as e:
        print("Insert Book Error:", e)
        return False
    finally:
        conn.close()

def update_book(book_id, title, isbn, publish_date, author_id):
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Books SET title=%s, isbn=%s, publish_date=%s, author_id=%s WHERE book_id=%s;", 
                       (title, isbn, publish_date, author_id, book_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error updating book: {e}")
        conn.close()
        return False

def delete_book(book_id):
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE book_id=%s;", (book_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error deleting book: {e}")
        conn.close()
        return False


def get_all_members():
    conn = connect()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Members;")
        result = cursor.fetchall()
        cursor.close()
        return result
    finally:
        conn.close()

def insert_member(name, card_number, email, phone):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Members (name, card_number, email, phone)
            VALUES (%s, %s, %s, %s);
        """, (name, card_number, email, phone))
        conn.commit()
        return True
    except Error as e:
        print("Insert Member Error:", e)
        return False
    finally:
        conn.close()

def update_member(member_id, name, card_number, email, phone):
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Members SET name=%s, card_number=%s, email=%s, phone=%s WHERE member_id=%s;", 
                       (name, card_number, email, phone, member_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error updating member: {e}")
        conn.close()
        return False

def delete_member(member_id):
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Members WHERE member_id=%s;", (member_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error deleting member: {e}")
        conn.close()
        return False


def get_checkout_history():
    conn = connect()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CheckoutHistory;")
        result = cursor.fetchall()
        cursor.close()
        return result
    finally:
        conn.close()

def insert_checkout(book_title, isbn, checkout_date, due_date, member_name):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO CheckoutHistory (book_title, isbn, checkout_date, due_date, member_name)
            VALUES (%s, %s, %s, %s, %s);
        """, (book_title, isbn, checkout_date, due_date, member_name))
        conn.commit()
        return True
    except Error as e:
        print("Insert Checkout Error:", e)
        return False
    finally:
        conn.close()


def get_overdue_books():
    conn = connect()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM OverdueBooks;")
        result = cursor.fetchall()
        cursor.close()
        return result
    finally:
        conn.close()

def insert_overdue(book_title, isbn, member_name, original_due_date, late_fees):
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO OverdueBooks (book_title, isbn, member_name, original_due_date, late_fees)
            VALUES (%s, %s, %s, %s, %s);
        """, (book_title, isbn, member_name, original_due_date, late_fees))
        conn.commit()
        return True
    except Error as e:
        print("Insert Overdue Error:", e)
        return False
    finally:
        conn.close()
