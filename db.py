import mysql.connector
from datetime import date

# Function to connect to MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",        # MySQL server host
            user="root",             # MySQL username
            password="Bradys36!",     # MySQL password
            database="library_db"    # The name of the database you created
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to initialize the database schema (create tables)
def initialize_db():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    # Create Authors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        country VARCHAR(255),
        birth_date DATE
    );
    ''')

    # Create Publishers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        country VARCHAR(255),
        website VARCHAR(255)
    );
    ''')

    # Create Books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        ISBN VARCHAR(255),
        publication_date DATE,
        publisher_id INT,
        FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    );
    ''')

    # Create Book_Authors table (many-to-many relationship)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book_Authors (
        book_id INT,
        author_id INT,
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    );
    ''')

    # Create Members table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        card_number VARCHAR(255) UNIQUE,
        email VARCHAR(255),
        phone VARCHAR(255)
    );
    ''')

    # Create OverdueBooks table to track overdue books
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OverdueBooks (
        overdue_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT,
        checkout_date DATE,
        due_date DATE,
        late_fees DECIMAL(10, 2),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    );
    ''')

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Database initialized successfully.")

# Function to insert sample data into the tables
def insert_sample_data():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    # Insert sample data into Authors table
    cursor.executemany('''
    INSERT IGNORE INTO Authors (first_name, last_name, country, birth_date) 
    VALUES (%s, %s, %s, %s);
    ''', [
        ('Jane', 'Austen', 'UK', '1775-12-16'),
        ('Mark', 'Twain', 'USA', '1835-11-30'),
        ('Charles', 'Dickens', 'UK', '1812-02-07'),
        ('Leo', 'Tolstoy', 'Russia', '1828-09-09'),
        ('James Edward', 'Austen-Leigh', 'UK', '1798-09-16')
    ])

    # Insert sample data into Publishers table
    cursor.executemany('''
    INSERT IGNORE INTO Publishers (name, country, website)
    VALUES (%s, %s, %s);
    ''', [
        ('Pearson', 'USA', 'https://www.pearson.com'),
        ('Penguin', 'UK', 'https://www.penguin.com'),
        ('Oxford University Press', 'UK', 'https://www.oup.com')
    ])

    # Insert sample data into Books table
    cursor.executemany('''
    INSERT IGNORE INTO Books (title, ISBN, publication_date, publisher_id) 
    VALUES (%s, %s, %s, %s);
    ''', [
        ('Pride and Prejudice', '978-1503290563', '1813-01-28', 1),
        ('Adventures of Huckleberry Finn', '978-1503211094', '1885-12-10', 2),
        ('Sense and Sensibility', '978-1501111105', '1811-10-30', 1),
        ('Emma', '978-0141439587', '1815-12-23', 1),
        ('Mansfield Park', '978-0141439809', '1814-07-09', 1),
        ('Great Expectations', '978-0141439564', '1861-08-01', 3),
        ('War and Peace', '978-0199232765', '1869-01-01', 3),
        ('The Watsons', '978-0192833805', '1871-01-01', 3)
    ])

    # Insert sample data into Book_Authors table
    cursor.executemany('''
    INSERT IGNORE INTO Book_Authors (book_id, author_id)
    VALUES (%s, %s);
    ''', [
        (1, 1),
        (2, 2),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 3),
        (7, 4),
        (8, 1),
        (8, 5)
    ])

    # Insert sample data into Members table
    cursor.executemany('''
    INSERT IGNORE INTO Members (name, card_number, email, phone)
    VALUES (%s, %s, %s, %s);
    ''', [
        ('Alice Johnson', '123456', 'alice@gmail.com', '555-1234'),
        ('Bob Smith', '234567', 'bob@gmail.com', '555-2345'),
        ('Charlie Brown', '345678', 'charlie@gmail.com', '555-3456'),
        ('David White', '456789', 'david@gmail.com', '555-4567'),
        ('Eve Black', '567890', 'eve@gmail.com', '555-5678')
    ])

    # Insert sample data into OverdueBooks table
    cursor.executemany('''
    INSERT IGNORE INTO OverdueBooks (book_id, checkout_date, due_date, late_fees)
    VALUES (%s, %s, %s, %s);
    ''', [
        (1, '2023-01-01', '2023-01-15', 5.00),
        (2, '2023-02-01', '2023-02-15', 3.50),
        (3, '2023-03-01', '2023-03-10', 2.00),
        (4, '2023-04-01', '2023-04-10', 4.00),
        (5, '2023-05-01', '2023-05-05', 1.00)
    ])

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Sample data inserted successfully.")

# Fetch all books from the database
def get_all_books():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return []

    cursor = conn.cursor(dictionary=True)  # This makes the result a list of dictionaries

    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books

# Fetch all members from the database
def get_all_members():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return []

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()

    cursor.close()
    conn.close()

    return members

# Fetch all overdue books from the database
def get_all_overdue_books():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return []

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM OverdueBooks")
    overdue_books = cursor.fetchall()

    cursor.close()
    conn.close()

    return overdue_books

# Test the functions by initializing the database and inserting sample data
if __name__ == "__main__":
    initialize_db()
    insert_sample_data()

    # Test fetch functions
    print("Fetching all books:")
    books = get_all_books()
    for book in books:
        print(book)

    print("\nFetching all members:")
    members = get_all_members()
    for member in members:
        print(member)

    print("\nFetching all overdue books:")
    overdue_books = get_all_overdue_books()
    for overdue_book in overdue_books:
        print(overdue_book)
