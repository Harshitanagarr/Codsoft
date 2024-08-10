import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List Application")
        master.geometry("400x400")
        master.configure(bg="#e0f7fa")

        self.frame = tk.Frame(master, bg="#e0f7fa")
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE,
            font=("Arial", 12), bg="#ffffff", fg="#000000",
            selectbackground="#b3e5fc", selectforeground="#000000"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(master, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.add_button = tk.Button(
            master, text="Add Task", command=self.add_task, 
            bg="#03a9f4", fg="#ffffff", font=("Arial", 12), bd=0, 
            activebackground="#0288d1"
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            master, text="Delete Task", command=self.delete_task, 
            bg="#f44336", fg="#ffffff", font=("Arial", 12), bd=0, 
            activebackground="#e53935"
        )
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(
            master, text="Clear All Tasks", command=self.clear_tasks, 
            bg="#ff9800", fg="#ffffff", font=("Arial", 12), bd=0, 
            activebackground="#fb8c00"
        )
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
