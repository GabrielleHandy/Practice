"""A number-guessing game."""
import random
# Put your code here

name = input("Hello!! What is your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")
num = random.randint(1, 100)
counter = 0
guess = int(input("Your guess? "))

while guess != num:
    if guess > num:
        print("Your guess is too high, try again.")
        guess = int(input("Your guess? "))
    elif guess < num:
        print("Your guess is too low, try again.")
        guess = int(input("Your guess? "))
    counter += 1

print(f"Well done, {name}! You found my number in {counter} tries!")