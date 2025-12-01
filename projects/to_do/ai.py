# todo_gui.py
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime

FILE_NAME = "tasks.txt"
DELIM = "|||"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                parts = line.split(DELIM)
                # expected: status ||| date ||| text
                if len(parts) >= 3:
                    status, date_str, text = parts[0], parts[1], DELIM.join(parts[2:])
                else:
                    # fallback: entire line is text
                    status, date_str, text = "0", "", parts[0]
                tasks.append({
                    "status": status,        # "1" done, "0" not done
                    "date": date_str,
                    "text": text
                })
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            line = f"{t['status']}{DELIM}{t['date']}{DELIM}{t['text']}\n"
            f.write(line)

class TodoApp:
    def __init__(self, root):
        self.root = root
        root.title("To-Do List")
        root.geometry("600x430")
        root.resizable(False, False)

        self.tasks = load_tasks()

        # top frame: input
        top = tk.Frame(root, padx=10, pady=8)
        top.pack(fill="x")

        self.entry = tk.Entry(top, font=("Segoe UI", 12))
        self.entry.pack(side="left", fill="x", expand=True)

        add_btn = tk.Button(top, text="Add Task", command=self.add_task)
        add_btn.pack(side="left", padx=6)

        # middle: listbox with scrollbar
        mid = tk.Frame(root, padx=10)
        mid.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(mid, font=("Consolas", 11), activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(mid, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # right side buttons
        right = tk.Frame(root, padx=10, pady=8)
        right.pack(fill="x")

        btn_frame = tk.Frame(right)
        btn_frame.pack(anchor="w")

        edit_btn = tk.Button(btn_frame, text="Edit", width=10, command=self.edit_task)
        edit_btn.grid(row=0, column=0, padx=4, pady=4)

        delete_btn = tk.Button(btn_frame, text="Delete", width=10, command=self.delete_task)
        delete_btn.grid(row=0, column=1, padx=4, pady=4)

        toggle_btn = tk.Button(btn_frame, text="Toggle Done", width=12, command=self.toggle_done)
        toggle_btn.grid(row=0, column=2, padx=4, pady=4)

        refresh_btn = tk.Button(btn_frame, text="Refresh", width=10, command=self.refresh)
        refresh_btn.grid(row=0, column=3, padx=4, pady=4)

        # bind double-click to toggle or edit
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_done())

        # status bar
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(root, textvariable=self.status_var, anchor="w", padx=10)
        self.status_label.pack(fill="x", side="bottom")
        
        self.refresh()

    def format_item(self, t):
        mark = "[X]" if t["status"] == "1" else "[ ]"
        date = t["date"] if t["date"] else "-"
        # show: [ ] 2025-11-29 21:00  - Task text
        return f"{mark} {date}  -  {t['text']}"

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            self.listbox.insert(tk.END, self.format_item(t))
        self.status_var.set(f"Tasks: {len(self.tasks)}  | File: {os.path.abspath(FILE_NAME)}")

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Empty", "Please enter a task.")
            return
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks.append({"status": "0", "date": now, "text": text})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.refresh()

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Select", "Please select a task to delete.")
            return
        idx = sel[0]
        txt = self.tasks[idx]['text']
        if messagebox.askyesno("Confirm", f"Delete task:\n\n{txt}\n\nAre you sure?"):
            self.tasks.pop(idx)
            save_tasks(self.tasks)
            self.refresh()

    def edit_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Select", "Please select a task to edit.")
            return
        idx = sel[0]
        old = self.tasks[idx]
        new_text = simpledialog.askstring("Edit task", "Edit task text:", initialvalue=old["text"], parent=self.root)
        if new_text is None:
            return  # cancelled
        new_text = new_text.strip()
        if new_text == "":
            messagebox.showwarning("Empty", "Task text cannot be empty.")
            return
        # update date to now to indicate modification
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks[idx]["text"] = new_text
        self.tasks[idx]["date"] = now
        save_tasks(self.tasks)
        self.refresh()

    def toggle_done(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Select", "Please select a task to toggle status.")
            return
        idx = sel[0]
        cur = self.tasks[idx]
        cur["status"] = "0" if cur["status"] == "1" else "1"
        # update date to show when toggled
        cur["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(self.tasks)
        self.refresh()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
