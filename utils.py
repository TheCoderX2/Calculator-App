# This file contains utility functions that can be used across your application

def validate_expression(expr):
    # Add validation logic here if needed
    pass

def save_history(history):
    # Optionally, save history to a file
    with open('history.txt', 'a') as file:
        file.write(history + "\n")
