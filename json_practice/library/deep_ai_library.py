import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_NAME = "library.json"

# ====================== DATA ======================
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ====================== GUI FUNCTIONS ======================
def refresh_list():
    listbox.delete(0, tk.END)
    data = load_data()
    for name, info in data.items():
        listbox.insert(
            tk.END,
            f"{name} | Available: {info['available']} | Borrowed: {info['borrowed']}"
        )

def add_book():
    data = load_data()

    name = simpledialog.askstring("Add Book", "Book title:")
    if not name:
        return

    try:
        copies = int(simpledialog.askstring("Copies", "Total copies:"))
        if copies <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid number!")
        return

    if name in data:
        data[name]["available"] += copies
        data[name]["total"] += copies
    else:
        data[name] = {
            "available": copies,
            "borrowed": 0,
            "total": copies
        }

    save_data(data)
    refresh_list()
    messagebox.showinfo("Success", "Book added successfully!")

def borrow_book():
    data = load_data()
    selection = listbox.curselection()

    if not selection:
        messagebox.showwarning("Warning", "Select a book first!")
        return

    book_name = listbox.get(selection[0]).split("|")[0].strip()
    book = data[book_name]

    if book["available"] == 0:
        messagebox.showerror("Error", "No available copies!")
        return

    try:
        num = int(simpledialog.askstring("Borrow", "Copies to borrow:"))
        if num <= 0 or num > book["available"]:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid number!")
        return

    book["available"] -= num
    book["borrowed"] += num
    save_data(data)
    refresh_list()
    messagebox.showinfo("Success", "Book borrowed!")

def return_book():
    data = load_data()
    selection = listbox.curselection()

    if not selection:
        messagebox.showwarning("Warning", "Select a book first!")
        return

    book_name = listbox.get(selection[0]).split("|")[0].strip()
    book = data[book_name]

    if book["borrowed"] == 0:
        messagebox.showerror("Error", "No borrowed copies!")
        return

    try:
        num = int(simpledialog.askstring("Return", "Copies to return:"))
        if num <= 0 or num > book["borrowed"]:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid number!")
        return

    book["available"] += num
    book["borrowed"] -= num
    save_data(data)
    refresh_list()
    messagebox.showinfo("Success", "Book returned!")

def delete_book():
    data = load_data()
    selection = listbox.curselection()

    if not selection:
        messagebox.showwarning("Warning", "Select a book first!")
        return

    book_name = listbox.get(selection[0]).split("|")[0].strip()

    if messagebox.askyesno("Confirm", f"Delete '{book_name}'?"):
        del data[book_name]
        save_data(data)
        refresh_list()

def search_book():
    term = search_entry.get().lower()
    listbox.delete(0, tk.END)

    data = load_data()
    for name, info in data.items():
        if term in name.lower():
            listbox.insert(
                tk.END,
                f"{name} | Available: {info['available']} | Borrowed: {info['borrowed']}"
            )

# ====================== GUI SETUP ======================
root = tk.Tk()
root.title("Library Management System")
root.geometry("650x450")
root.resizable(False, False)

title = tk.Label(root, text="📚 Library Management System", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

listbox = tk.Listbox(frame, width=80, height=12)
listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Book", width=12, command=add_book).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Borrow", width=12, command=borrow_book).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Return", width=12, command=return_book).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_book).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(search_frame, text="Search", command=search_book).pack(side=tk.LEFT)

refresh_list()
root.mainloop()
