import mysql.connector

print("Script started")

# Function to connect to MySQL database
def connect_to_db():
    print("Connecting to DB...")
    try:
        conn = mysql.connector.connect(
            host="localhost",        
            user="root",             
            password="",    
            database="library_db"    
        )
        print("Connected to the database.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Function to initialize the database schema (create tables)
def initialize_db():
    print("Initializing database schema...")
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database. Initialization skipped.")
        return

    cursor = conn.cursor()

    # Create Authors table
    print("Creating Authors table...")
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
    print("Creating Publishers table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        country VARCHAR(255),
        website VARCHAR(255)
    );
    ''')

    # Create Books table
    print("Creating Books table...")
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
    print("Creating Book_Authors table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book_Authors (
        book_id INT,
        author_id INT,
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print("Database schema initialized successfully.")

# Function to insert sample data into the tables
def insert_sample_data():
    print("Inserting sample data...")
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database. Insertion skipped.")
        return

    cursor = conn.cursor()

    # Insert sample data into Authors table
    print("Inserting into Authors...")
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
    print("Inserting into Publishers...")
    cursor.executemany('''
    INSERT IGNORE INTO Publishers (name, country, website)
    VALUES (%s, %s, %s);
    ''', [
        ('Pearson', 'USA', 'https://www.pearson.com'),
        ('Penguin', 'UK', 'https://www.penguin.com'),
        ('Oxford University Press', 'UK', 'https://www.oup.com')
    ])

    # Insert sample data into Books table
    print("Inserting into Books...")
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
    print("Inserting into Book_Authors...")
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

    conn.commit()
    cursor.close()
    conn.close()
    print("Sample data inserted successfully.")

# Run everything
if __name__ == "__main__":
    print("Main block started")
    initialize_db()
    insert_sample_data()
    print("Script completed")
