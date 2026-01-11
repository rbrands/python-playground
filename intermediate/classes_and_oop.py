#!/usr/bin/env python3
"""
Classes and Object-Oriented Programming in Python
This demonstrates basic OOP concepts in Python.
"""

class Dog:
    """A simple class representing a dog."""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a new Dog instance."""
        self.name = name  # Instance variable
        self.age = age
    
    def description(self):
        """Return a description of the dog."""
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        """Make the dog speak."""
        return f"{self.name} says {sound}"

class BankAccount:
    """A class representing a simple bank account."""
    
    def __init__(self, owner, balance=0):
        """Initialize a bank account."""
        self.owner = owner
        self._balance = balance  # Convention: _ indicates "private"
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance."""
        return self._balance
    
    def __str__(self):
        """String representation of the account."""
        return f"BankAccount(owner={self.owner}, balance=${self._balance})"

class Rectangle:
    """A class representing a rectangle with properties."""
    
    def __init__(self, width, height):
        """Initialize a rectangle."""
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """Get the width."""
        return self._width
    
    @property
    def height(self):
        """Get the height."""
        return self._height
    
    @property
    def area(self):
        """Calculate and return the area."""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self._width + self._height)

def main():
    """Demonstrate OOP concepts."""
    print("=== Object-Oriented Programming ===\n")
    
    # Dog class
    print("--- Dog Class ---")
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Lucy", 5)
    
    print(dog1.description())
    print(dog2.description())
    print(dog1.speak("Woof!"))
    print(f"Species: {Dog.species}\n")
    
    # BankAccount class
    print("--- Bank Account ---")
    account = BankAccount("Alice", 1000)
    print(account)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Current balance: ${account.get_balance()}\n")
    
    # Rectangle with properties
    print("--- Rectangle with Properties ---")
    rect = Rectangle(5, 10)
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")

if __name__ == "__main__":
    main()
