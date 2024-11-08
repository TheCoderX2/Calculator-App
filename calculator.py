import math

class Calculator:
    def __init__(self):
        self.history = []  # Store calculation history

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append(f"Error: Division by zero")
            return "Error"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def sqrt(self, a):
        if a < 0:
            self.history.append(f"Error: Negative number for square root")
            return "Error"
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result

    def power(self, a, b):
        result = math.pow(a, b)
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def sin(self, a):
        result = math.sin(math.radians(a))
        self.history.append(f"sin({a}°) = {result}")
        return result

    def cos(self, a):
        result = math.cos(math.radians(a))
        self.history.append(f"cos({a}°) = {result}")
        return result

    def tan(self, a):
        result = math.tan(math.radians(a))
        self.history.append(f"tan({a}°) = {result}")
        return result

    def log(self, a, base=10):
        if a <= 0:
            self.history.append(f"Error: Log of non-positive number")
            return "Error"
        result = math.log(a, base)
        self.history.append(f"log({a}, {base}) = {result}")
        return result

    def factorial(self, a):
        if a < 0:
            self.history.append(f"Error: Factorial of negative number")
            return "Error"
        result = math.factorial(a)
        self.history.append(f"{a}! = {result}")
        return result

    def get_history(self):
        return "\n".join(self.history)
