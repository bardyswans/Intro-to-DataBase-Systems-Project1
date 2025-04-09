import tkinter as tk
from tkinter import ttk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("800x600")  # Width x Height

    
    title_label = ttk.Label(root, text="📚 Library Management System", font=("Helvetica", 18))
    title_label.pack(pady=20)

    content_frame = ttk.Frame(root, padding=10, relief="ridge")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    
    placeholder_label = ttk.Label(content_frame, text="Main Content Goes Here", font=("Helvetica", 14))
    placeholder_label.place(relx=0.5, rely=0.5, anchor="center")

   
    root.mainloop()

if __name__ == "__main__":
    main()
