import mysql.connector
from mysql.connector import Error

# Replace these with your own database connection details
DB_CONFIG = {
    'host': 'localhost',       # Database host
    'user': 'root',            # Database user
    'password': 'Bradys36!',   # Database password
    'database': 'library_db'   # Database name
}

# Connect to the database
def connect():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

        ('Eve Black', '567890', 'eve@gmail.com', '555-5678')
# Fetch all books from the Books table
def get_all_books():
    conn = connect()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT book_id, title, ISBN, publication_date, publisher_id FROM Books;")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books
    except Error as e:
        print(f"Error fetching books: {e}")
        conn.close()
        return []

# Fetch all members from the Members table
def get_all_members():
    conn = connect()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT member_id, name, card_number, email, phone FROM Members;")
        members = cursor.fetchall()
        cursor.close()
        conn.close()
        return members
    except Error as e:
        print(f"Error fetching members: {e}")
        conn.close()
        return []

# Insert a new book into the Books table
def insert_book(title, isbn, publish_date, author_id):
    conn = connect()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, isbn, publish_date, author_id) VALUES (%s, %s, %s, %s);", 
                       (title, isbn, publish_date, author_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error inserting book: {e}")
        conn.close()
        return False

# Insert a new member into the Members table
def insert_member(first_name, last_name, email):
    conn = connect()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Members (first_name, last_name, email) VALUES (%s, %s, %s);", 
                       (first_name, last_name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error inserting member: {e}")
        conn.close()
        return False

# Insert sample data for books and members if tables are empty
def insert_sample_data():
    books = get_all_books()
    if not books:
        print("Inserting sample books...")
        insert_book('Pride and Prejudice', '978-1503290563', '1813-01-28', 1)
        insert_book('Adventures of Huckleberry Finn', '978-1503211094', '1885-12-10', 2)

    members = get_all_members()
    if not members:
        print("Inserting sample members...")
        insert_member('John', 'Doe', 'john.doe@example.com')
        insert_member('Jane', 'Smith', 'jane.smith@example.com')

# Call this function to insert data if tables are empty
insert_sample_data()
