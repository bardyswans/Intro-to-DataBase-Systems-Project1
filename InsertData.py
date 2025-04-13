from db import insert_book, insert_member, insert_checkout, insert_overdue

# Books
insert_book("1984", "George Orwell", "9780451524935", False)
insert_book("The Hobbit", "J.R.R. Tolkien", "9780261102217", True)

# Members
insert_member("Alice Johnson", "CARD001", "alice@gmail.com", "555-1234")
insert_member("Bob Smith", "CARD002", "bob@gmail.com", "555-5678")

# Checkout History
insert_checkout("The Hobbit", "9780261102217", "2024-04-01", "2024-04-08", "Bob Smith")

# Overdue Books
insert_overdue("The Hobbit", "9780261102217", "Bob Smith", "2024-04-08", 4.50)

print("Sample data inserted.")
