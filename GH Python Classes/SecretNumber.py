import random

attempts = 0;
maxAttempts=5
randomNum=random.randrange(1, 100)

print("System is generating a number between 1 and 100.")

while attempts < maxAttempts:

    guess = int(input(" Enter your guess: "))
    attempts += 1

    if guess < randomNum:
        print("Too low!")
    elif guess > randomNum:
        print("Too high!")
    else:
        print(f"Correct! You won in {attempts} tries.")
        break

if guess != randomNum:
    print(f"Game over. The number was {randomNum}.")



