"""A number-guessing game."""
import random

#initialize empty list of player scores
scores = []

def main():
    """"play game"""
    # only greet player on their first game
    if len(scores) == 0:
        name = greet()

    # count number of tries
    counter = 1

    # randomizes number btw 1 and 100
    num = random.randint(1, 100)

    # call first user guess
    guess = validate_input()

    # check guesses
    while guess != num:
        counter += 1
        if guess > num:
            print("Your guess is too high, try again.")
            guess = validate_input()
        elif guess < num:
            print("Your guess is too low, try again.")
            guess = validate_input()

    # add current games score to scores list
    scores.append(counter)

    # trying to get a high score but when we recall the main function doesnt keep it   
    update_score(scores, counter)

    # congratulate user for correct guess
    print(f"Well done! You found my number in {counter} tries!")

    # ask if user wants to play again
    again = input("Play again? ")
    if again.lower() in ["yes", "y"]:
        main()

def greet():
    """greet user"""
    name = input("Hello! What is your name? ")
    print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")
    return name

def update_score(scores, counter):
    """returning player's best score"""
    if counter <= min(scores):
        print(f"New High Score!: {counter}")
    
def validate_input():
    """calls guess function and checks faulty entry"""
    answer = input("Your guess? ")
    while answer.isdigit() is False:
        print("Numbers only yo")
        answer = input("Your guess? ")
    return int(answer)

if __name__ == "__main__":
    main()