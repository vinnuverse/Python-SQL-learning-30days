# day2_multiplication_table.py

print("📊 Multiplication Table Generator")

while True:
    # 1. Take input from user
    num_input = input("Enter a number to print its multiplication table: ")

    # 2. Check if input is valid number
    try:
        num = int(num_input)
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        continue

    # 3. Print multiplication table
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    # 4. Ask if user wants to do another
    again = input("\nWould you like to generate another table? (yes/no): ").strip().lower()
    if again != "yes":
        print("✅ Thank you for using the Multiplication Table Generator! 👋")
        break
# This code generates a multiplication table for a user-specified number and allows the user to generate multiple tables if desired.