import mysql.connector
from mysql.connector import Error

schema_sql = """

DROP TABLE IF EXISTS Books;
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(50),
    is_checked_out BOOLEAN
);

CREATE TABLE IF NOT EXISTS Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    card_number VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS CheckoutHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(255),
    isbn VARCHAR(50),
    checkout_date DATE,
    due_date DATE,
    member_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS OverdueBooks (
    overdue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(255),
    isbn VARCHAR(50),
    member_name VARCHAR(255),
    original_due_date DATE,
    late_fees DECIMAL(10, 2)
);
"""

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bradys36!",  
        database="library_db"
    )
    cursor = conn.cursor()
    for statement in schema_sql.strip().split(';'):
        if statement.strip():
            cursor.execute(statement + ';')
    conn.commit()
    print("Tables created successfully.")
except Error as e:
    print("MySQL Error:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
