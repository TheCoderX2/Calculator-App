import tkinter as tk
from tkinter import messagebox

class CalculatorUI:
    def __init__(self, root, calculator):
        self.root = root
        self.calculator = calculator

        # Create the display screen
        self.display = tk.Entry(self.root, width=40, borderwidth=5, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons layout
        self.create_buttons()

    def create_buttons(self):
        # Define button texts and their corresponding functions
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('log', 6, 0), ('^', 6, 1), ('!', 6, 2), ('CLR', 6, 3)
        ]
        
        # Create the buttons dynamically
        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, width=10, height=3, font=('Arial', 14), 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, button_text):
        if button_text == '=':
            self.calculate()
        elif button_text == 'CLR':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, button_text)

    def calculate(self):
        expression = self.display.get()
        try:
            result = self.evaluate_expression(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.display.delete(0, tk.END)

    def evaluate_expression(self, expression):
        # Convert text to appropriate function calls
        if expression == "sin":
            return self.calculator.sin(float(self.display.get()))
        if expression == "cos":
            return self.calculator.cos(float(self.display.get()))
        if expression == "tan":
            return self.calculator.tan(float(self.display.get()))
        # Add more advanced operations here

        # Otherwise, use eval (caution in production)
        return eval(expression)  # For simplicity, eval is used here

