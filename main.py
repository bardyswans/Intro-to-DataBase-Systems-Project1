import tkinter as tk
from tkinter import ttk
from db import get_all_books  # Import the fetch function

def display_books(frame):
    # Clear previous widgets (if refreshing)
    for widget in frame.winfo_children():
        widget.destroy()

    # Fetch all books from the database
    books = get_all_books()

    # Define columns
    columns = ("book_id", "title", "ISBN", "publication_date", "publisher_id")

    # Create the Treeview widget
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Define headings
    tree.heading("book_id", text="Book ID")
    tree.heading("title", text="Title")
    tree.heading("ISBN", text="ISBN")
    tree.heading("publication_date", text="Publication Date")
    tree.heading("publisher_id", text="Publisher ID")

    # Set column widths
    tree.column("book_id", width=80, anchor="center")
    tree.column("title", width=200)
    tree.column("ISBN", width=150)
    tree.column("publication_date", width=120, anchor="center")
    tree.column("publisher_id", width=100, anchor="center")

    # Insert data into the tree
    for book in books:
        tree.insert("", "end", values=book)

    # Add scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Pack widgets
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def main():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("900x600")

    title_label = ttk.Label(root, text="📚 Library Management System", font=("Helvetica", 18))
    title_label.pack(pady=10)

    content_frame = ttk.Frame(root, padding=10, relief="ridge")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Show books on launch
    display_books(content_frame)

    root.mainloop()

if __name__ == "__main__":
    main()
