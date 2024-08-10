import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x200")
        self.master.configure(bg="#e3f2fd")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self.master, text="Enter desired password length:", 
            font=("Arial", 14), bg="#e3f2fd"
        )
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(self.master, font=("Arial", 14), width=10)
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(
            self.master, text="Generate Password", command=self.generate_password, 
            font=("Arial", 14), bg="#42a5f5", fg="#ffffff", borderwidth=2
        )
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.master, text="", font=("Arial", 14), bg="#e3f2fd")
        self.password_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for the length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
