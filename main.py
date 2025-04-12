import tkinter as tk
from tkinter import ttk
from db import get_all_books, get_all_members

# Function to display books
def display_books(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    books = get_all_books()

    columns = ("Book ID", "Title", "ISBN", "Publication Date", "Publisher ID")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for book in books:
        tree.insert('', tk.END, values=book)

    tree.pack(expand=True, fill='both')

# Function to display members
def display_members(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    members = get_all_members()

    columns = ("Member ID", "Name", "Card Number", "Email", "Phone")
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for member in members:
        tree.insert('', tk.END, values=member)

    tree.pack(expand=True, fill='both')

# Main GUI setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")

# Tabs
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Books Tab
books_frame = ttk.Frame(notebook)
notebook.add(books_frame, text='Books')
display_books(books_frame)

# Members Tab
members_frame = ttk.Frame(notebook)
notebook.add(members_frame, text='Members')
display_members(members_frame)

root.mainloop()
