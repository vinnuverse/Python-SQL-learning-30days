# Day 1: Python Basics in VS Code

# -----------------------------------
# 1. Variables & Data Types
# -----------------------------------
name = "Tiwari"
age = 27
height = 5.9
is_learning = True

print("Hi,", name)
print("Age:", age)
print("Height:", height, "ft")
print("Learning Python:", is_learning)

# -----------------------------------
# 2. User Input
# -----------------------------------
your_name = input("\nEnter your name: ")
print("Hello", your_name, "! Welcome to Day 1 of your Python journey.")

# -----------------------------------
# 3. Simple Calculator
# -----------------------------------
print("\n--- Simple Calculator ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Quotient:", a / b)
    print("Modulus:", a % b)
else:
    print("Division and modulus not allowed (b is zero).")
print("Power (a^b):", a ** b)

# -----------------------------------
# 4. Bonus: Star Pattern
# -----------------------------------
print("\n--- Star Pattern ---")
for i in range(1, 6):
    print("*" * i)
