import mysql.connector

print("Starting MySQL test script...")  # Debugging message

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",  # or your MySQL host (e.g., "127.0.0.1")
        user="root",  # replace with your MySQL username
        password="",  # replace with your MySQL password
        database="library_db"  # replace with your database name
    )
    
    # If the connection is successful, print a success message
    if conn.is_connected():
        print("Successfully connected to the database!")
    
    # Create a cursor object and execute a simple query to test
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"Currently using the database: {db_name[0]}")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
