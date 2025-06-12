print("Welcome to the Smart Unit Converter!")

name = input("Enter your name: ")
print(f"Hello {name}, what would you like to convert today?")

while True:
    print("\n1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles:.2f} miles.")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")

    elif choice == "3":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is equal to {pounds:.2f} pounds.")

    elif choice == "4":
        print("\nThank you for using the Smart Unit Converter!")
        print("Exiting the converter. Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
        continue  # Skip asking to continue on invalid input

    again = input("\nWould you like to convert another value? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye, have a great day! 👋")
        break

# This code is a simple unit converter that allows users to convert between kilometers and miles, Celsius and Fahrenheit, and kilograms and pounds.
