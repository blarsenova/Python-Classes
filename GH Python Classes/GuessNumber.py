import random

def guess_the_number():
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I have picked a number between 1 and 100. Try to guess it.")

    # Loop continues until the user's guess matches the secret number
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)
            attempts += 1

            # Provide feedback to the user
            if guess < secret_number:
                print("Too low, try again.\n")
            elif guess > secret_number:
                print("Too high, try again.\n")
            else:
                # The loop breaks when the guess is correct
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
        except ValueError:
            # Handle non-integer input gracefully
            print("Invalid input. Please enter a valid integer.\n")

if __name__ == "__main__":
    guess_the_number()