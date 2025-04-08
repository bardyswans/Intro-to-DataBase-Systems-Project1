import sqlite3

def initialize_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        is_checked_out INTEGER DEFAULT 0
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        card_number TEXT UNIQUE NOT NULL,
        email TEXT,
        phone TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CheckoutHistory (
        history_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        member_id INTEGER,
        checkout_date TEXT,
        due_date TEXT,
        FOREIGN KEY(book_id) REFERENCES Books(book_id),
        FOREIGN KEY(member_id) REFERENCES Members(member_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OverdueBooks (
        overdue_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        member_id INTEGER,
        due_date TEXT,
        late_fee REAL,
        FOREIGN KEY(book_id) REFERENCES Books(book_id),
        FOREIGN KEY(member_id) REFERENCES Members(member_id)
    );
    ''')

    conn.commit()
    conn.close()
