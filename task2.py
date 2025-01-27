import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x400")
        self.master.configure(bg="#e3f2fd")

        self.create_widgets()

    def create_widgets(self):
        self.entry1 = tk.Entry(self.master, width=10, font=("Arial", 18), borderwidth=2)
        self.entry1.pack(pady=10)

        self.entry2 = tk.Entry(self.master, width=10, font=("Arial", 18), borderwidth=2)
        self.entry2.pack(pady=10)

        self.operations = ["+", "-", "*", "/"]
        self.operation_var = tk.StringVar(value=self.operations[0])
        self.operation_menu = tk.OptionMenu(self.master, self.operation_var, *self.operations)
        self.operation_menu.configure(font=("Arial", 14), bg="#bbdefb", borderwidth=2)
        self.operation_menu.pack(pady=10)

        self.calc_button = tk.Button(
            self.master, text="Calculate", command=self.calculate, 
            font=("Arial", 16), bg="#42a5f5", fg="#ffffff", borderwidth=2
        )
        self.calc_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 16), bg="#e3f2fd")
        self.result_label.pack(pady=20)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
