# Day 2: Bonus 🎮 Guess the Number Game (with Replay Option)

import random

print("🎮 Welcome to the Guess the Number Game!")

# Game replay loop
while True:
    print("\nI have picked a number between 1 and 10. Can you guess it?")

    # Step 1: Generate random number
    secret_number = random.randint(1, 10)
    attempts = 0

    # Step 2: Start guessing loop
    while True:
        guess_input = input("👉 Enter your guess (1-10): ")

        # Step 3: Validate input
        try:
            guess = int(guess_input)
        except ValueError:
            print("❌ Please enter a valid number between 1 and 10.")
            continue

        # Step 4: Count the attempt
        attempts += 1

        # Step 5: Check guess
        if guess < 1 or guess > 10:
            print("⚠️ Guess should be between 1 and 10.")
        elif guess < secret_number:
            print("🔼 Too low! Try again.")
        elif guess > secret_number:
            print("🔽 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempt(s).")
            break

    # Step 6: Ask if the user wants to play again
    play_again = input("\n🔁 Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n✅ Thanks for playing! Goodbye 👋")
        break
# This code implements a simple "Guess the Number" game where the user has to guess a randomly generated number between 1 and 10.