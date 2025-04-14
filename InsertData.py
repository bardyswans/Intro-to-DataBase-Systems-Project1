from db import insert_book, insert_member, insert_checkout, insert_overdue

# --- Books (10) ---
insert_book("1984", "George Orwell", "9780451524935", 0)
insert_book("The Hobbit", "J.R.R. Tolkien", "9780261102217", 1)
insert_book("Fahrenheit 451", "Ray Bradbury", "9781451673319", 0)
insert_book("Brave New World", "Aldous Huxley", "9780060850524", 1)
insert_book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 0)
insert_book("Animal Farm", "George Orwell", "9780451526342", 1)
insert_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 0)
insert_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1)
insert_book("Moby Dick", "Herman Melville", "9781503280786", 0)
insert_book("The Giver", "Lois Lowry", "9780544336261", 1)

# --- Members (10) ---
insert_member("Alice Johnson", "CARD001", "alice@gmail.com", "555-1234")
insert_member("Bob Smith", "CARD002", "bob@gmail.com", "555-5678")
insert_member("Cathy Miller", "CARD003", "cathy@gmail.com", "555-4321")
insert_member("David Jones", "CARD004", "david@gmail.com", "555-6789")
insert_member("Eva Brown", "CARD005", "eva@gmail.com", "555-7890")
insert_member("Frank Wilson", "CARD006", "frank@gmail.com", "555-8765")
insert_member("Grace Lee", "CARD007", "grace@gmail.com", "555-3456")
insert_member("Henry Adams", "CARD008", "henry@gmail.com", "555-2109")
insert_member("Isla Thompson", "CARD009", "isla@gmail.com", "555-9876")
insert_member("Jake White", "CARD010", "jake@gmail.com", "555-6543")

# --- Checkout History (10) ---
insert_checkout("The Hobbit", "9780261102217", "2024-04-01", "2024-04-08", "Bob Smith")
insert_checkout("Fahrenheit 451", "9781451673319", "2024-04-03", "2024-04-10", "Cathy Miller")
insert_checkout("Brave New World", "9780060850524", "2024-04-05", "2024-04-12", "David Jones")
insert_checkout("Animal Farm", "9780451526342", "2024-04-07", "2024-04-14", "Eva Brown")
insert_checkout("The Catcher in the Rye", "9780316769488", "2024-04-08", "2024-04-15", "Frank Wilson")
insert_checkout("The Giver", "9780544336261", "2024-04-10", "2024-04-17", "Grace Lee")
insert_checkout("To Kill a Mockingbird", "9780061120084", "2024-04-02", "2024-04-09", "Alice Johnson")
insert_checkout("The Great Gatsby", "9780743273565", "2024-04-04", "2024-04-11", "Henry Adams")
insert_checkout("Moby Dick", "9781503280786", "2024-04-06", "2024-04-13", "Isla Thompson")
insert_checkout("1984", "9780451524935", "2024-04-01", "2024-04-08", "Jake White")

# --- Overdue Books (5) ---
insert_overdue("The Hobbit", "9780261102217", "Bob Smith", "2024-04-08")
insert_overdue("Fahrenheit 451", "9781451673319", "Cathy Miller", "2024-04-10")
insert_overdue("Animal Farm", "9780451526342", "Eva Brown", "2024-04-14")
insert_overdue("To Kill a Mockingbird", "9780061120084", "Alice Johnson", "2024-04-09")
insert_overdue("1984", "9780451524935", "Jake White", "2024-04-08")

print("✅ Sample data inserted successfully.")
