import random

answer = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))

if guess == answer:
    print("Correct!")
else:
    print("Wrong! The answer was", answer)
