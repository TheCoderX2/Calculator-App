import tkinter as tk
from ui import CalculatorUI
from calculator import Calculator

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Advanced Calculator")
    root.geometry("500x600")
    root.iconbitmap("resources/calculator.ico")  # Optional: add an icon

    # Initialize the Calculator Logic
    calc = Calculator()

    # Initialize the UI with the root window and calculator logic
    app = CalculatorUI(root, calc)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

