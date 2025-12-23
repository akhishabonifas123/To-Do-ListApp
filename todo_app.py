import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 2: Simple To-Do List")
        self.root.geometry("400x450")

        # Task storage
        self.tasks = []

        # --- UI Elements ---
        self.label = tk.Label(root, text="Enter Task Below:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.listbox.pack(pady=10, padx=20)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)  # Clear input field
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def update_listbox(self):
        # Clear the listbox and re-add all tasks
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
