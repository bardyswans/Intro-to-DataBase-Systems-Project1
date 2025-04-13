
import tkinter as tk
from tkinter import ttk, messagebox
from db import (
    get_all_books, insert_book, delete_book,
    get_all_members, insert_member, delete_member,
    get_checkout_history, insert_checkout,
    get_overdue_books, insert_overdue
)

def populate_tree(tree, columns, rows):
    tree.delete(*tree.get_children())
    tree["columns"] = columns
    tree["show"] = "headings"
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    for row in rows:
        tree.insert("", tk.END, values=row)

def create_books_tab(notebook):
    tab = ttk.Frame(notebook)
    tree = ttk.Treeview(tab)
    tree.pack(fill="both", expand=True)

    def refresh():
        populate_tree(tree, ["ID", "Title", "Author", "ISBN", "Checked Out"], get_all_books())

    def add_book():
        def submit():
            if insert_book(title.get(), author.get(), isbn.get(), is_checked_out.get()):
                messagebox.showinfo("Success", "Book added!")
                win.destroy()
                refresh()
            else:
                messagebox.showerror("Error", "Failed to add book.")

        win = tk.Toplevel()
        win.title("Add Book")
        tk.Label(win, text="Title").grid(row=0, column=0)
        tk.Label(win, text="Author").grid(row=1, column=0)
        tk.Label(win, text="ISBN").grid(row=2, column=0)
        tk.Label(win, text="Checked Out (0 or 1)").grid(row=3, column=0)

        title = tk.Entry(win); title.grid(row=0, column=1)
        author = tk.Entry(win); author.grid(row=1, column=1)
        isbn = tk.Entry(win); isbn.grid(row=2, column=1)
        is_checked_out = tk.Entry(win); is_checked_out.grid(row=3, column=1)

        tk.Button(win, text="Submit", command=submit).grid(row=4, column=1)

    def delete_selected():
        selected = tree.selection()
        if selected:
            book_id = tree.item(selected[0])["values"][0]
            if delete_book(book_id):
                messagebox.showinfo("Deleted", "Book deleted.")
                refresh()

    btns = ttk.Frame(tab)
    btns.pack(pady=5)
    ttk.Button(btns, text="Add Book", command=add_book).pack(side="left", padx=5)
    ttk.Button(btns, text="Delete Book", command=delete_selected).pack(side="left", padx=5)
    ttk.Button(btns, text="Refresh", command=refresh).pack(side="left", padx=5)

    refresh()
    return tab

def create_members_tab(notebook):
    tab = ttk.Frame(notebook)
    tree = ttk.Treeview(tab)
    tree.pack(fill="both", expand=True)

    def refresh():
        populate_tree(tree, ["ID", "Name", "Card #", "Email", "Phone"], get_all_members())

    def add_member():
        def submit():
            if insert_member(name.get(), card.get(), email.get(), phone.get()):
                messagebox.showinfo("Success", "Member added!")
                win.destroy()
                refresh()
            else:
                messagebox.showerror("Error", "Failed to add member.")

        win = tk.Toplevel()
        win.title("Add Member")
        tk.Label(win, text="Name").grid(row=0, column=0)
        tk.Label(win, text="Card #").grid(row=1, column=0)
        tk.Label(win, text="Email").grid(row=2, column=0)
        tk.Label(win, text="Phone").grid(row=3, column=0)

        name = tk.Entry(win); name.grid(row=0, column=1)
        card = tk.Entry(win); card.grid(row=1, column=1)
        email = tk.Entry(win); email.grid(row=2, column=1)
        phone = tk.Entry(win); phone.grid(row=3, column=1)

        tk.Button(win, text="Submit", command=submit).grid(row=4, column=1)

    def delete_selected():
        selected = tree.selection()
        if selected:
            member_id = tree.item(selected[0])["values"][0]
            if delete_member(member_id):
                messagebox.showinfo("Deleted", "Member deleted.")
                refresh()

    btns = ttk.Frame(tab)
    btns.pack(pady=5)
    ttk.Button(btns, text="Add Member", command=add_member).pack(side="left", padx=5)
    ttk.Button(btns, text="Delete Member", command=delete_selected).pack(side="left", padx=5)
    ttk.Button(btns, text="Refresh", command=refresh).pack(side="left", padx=5)

    refresh()
    return tab

def create_checkout_tab(notebook):
    tab = ttk.Frame(notebook)
    tree = ttk.Treeview(tab)
    tree.pack(fill="both", expand=True)

    def refresh():
        populate_tree(tree, ["ID", "Title", "ISBN", "Checkout", "Due", "Member"], get_checkout_history())

    def add_checkout():
        def submit():
            if insert_checkout(title.get(), isbn.get(), checkout.get(), due.get(), member.get()):
                messagebox.showinfo("Success", "Checkout added!")
                win.destroy()
                refresh()
            else:
                messagebox.showerror("Error", "Failed to add checkout.")

        win = tk.Toplevel()
        win.title("Add Checkout Record")
        tk.Label(win, text="Book Title").grid(row=0, column=0)
        tk.Label(win, text="ISBN").grid(row=1, column=0)
        tk.Label(win, text="Checkout Date (YYYY-MM-DD)").grid(row=2, column=0)
        tk.Label(win, text="Due Date (YYYY-MM-DD)").grid(row=3, column=0)
        tk.Label(win, text="Member").grid(row=4, column=0)

        title = tk.Entry(win); title.grid(row=0, column=1)
        isbn = tk.Entry(win); isbn.grid(row=1, column=1)
        checkout = tk.Entry(win); checkout.grid(row=2, column=1)
        due = tk.Entry(win); due.grid(row=3, column=1)
        member = tk.Entry(win); member.grid(row=4, column=1)

        tk.Button(win, text="Submit", command=submit).grid(row=5, column=1)

    btns = ttk.Frame(tab)
    btns.pack(pady=5)
    ttk.Button(btns, text="Add Checkout", command=add_checkout).pack(side="left", padx=5)
    ttk.Button(btns, text="Refresh", command=refresh).pack(side="left", padx=5)

    refresh()
    return tab

def create_overdue_tab(notebook):
    tab = ttk.Frame(notebook)
    tree = ttk.Treeview(tab)
    tree.pack(fill="both", expand=True)

    def refresh():
        populate_tree(tree, ["ID", "Title", "ISBN", "Member", "Due", "Late Fee"], get_overdue_books())

    def add_overdue():
        def submit():
            if insert_overdue(title.get(), isbn.get(), member.get(), due.get(), fees.get()):
                messagebox.showinfo("Success", "Overdue entry added!")
                win.destroy()
                refresh()
            else:
                messagebox.showerror("Error", "Failed to add overdue.")

        win = tk.Toplevel()
        win.title("Add Overdue Record")
        tk.Label(win, text="Book Title").grid(row=0, column=0)
        tk.Label(win, text="ISBN").grid(row=1, column=0)
        tk.Label(win, text="Member").grid(row=2, column=0)
        tk.Label(win, text="Original Due Date").grid(row=3, column=0)
        tk.Label(win, text="Late Fees").grid(row=4, column=0)

        title = tk.Entry(win); title.grid(row=0, column=1)
        isbn = tk.Entry(win); isbn.grid(row=1, column=1)
        member = tk.Entry(win); member.grid(row=2, column=1)
        due = tk.Entry(win); due.grid(row=3, column=1)
        fees = tk.Entry(win); fees.grid(row=4, column=1)

        tk.Button(win, text="Submit", command=submit).grid(row=5, column=1)

    btns = ttk.Frame(tab)
    btns.pack(pady=5)
    ttk.Button(btns, text="Add Overdue", command=add_overdue).pack(side="left", padx=5)
    ttk.Button(btns, text="Refresh", command=refresh).pack(side="left", padx=5)

    refresh()
    return tab

def show_main_window():
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1200x700")
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    notebook.add(create_books_tab(notebook), text="Books")
    notebook.add(create_members_tab(notebook), text="Members")
    notebook.add(create_checkout_tab(notebook), text="Checkout History")
    notebook.add(create_overdue_tab(notebook), text="Overdue Books")

    root.mainloop()
