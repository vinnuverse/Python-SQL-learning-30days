# Day 2: Python Conditions & Loops 💻🐍

print("🧠 Age Category Checker")

# 1. Ask user for their age with error handling
while True:
    age_input = input("Please enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("❌ That's not a valid number. Please enter a numeric age.")

# 2. Determine the category using if/elif/else
if age < 13:
    category = "Child"
elif 13 <= age <= 17:
    category = "Teenager"
elif 18 <= age <= 60:
    category = "Adult"
else:
    category = "Senior Citizen"

# 3. Print the result
print(f"You are classified as: {category}")

# 4. Ask if the user wants to check another age
while True:
    again = input("Would you like to check another age? (yes/no): ").strip().lower()

    if again == "yes":
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)
            if age < 13:
                category = "Child"
            elif 13 <= age <= 17:
                category = "Teenager"
            elif 18 <= age <= 60:
                category = "Adult"
            else:
                category = "Senior Citizen"
            print(f"You are classified as: {category}")
        except ValueError:
            print("❌ That's not a valid number. Please enter a numeric age.")

    elif again == "no":
        print("✅ Thank you for using the Age Category Checker! Goodbye! 👋")
        break
    else:
        print("❌ Invalid input. Please type 'yes' or 'no'.")

# This code checks the age category of a user based on their input and allows them to check multiple ages if desired.