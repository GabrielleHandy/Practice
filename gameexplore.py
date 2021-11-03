"""A number-guessing game."""
import random

#initialize empty list of player scores
scores = []

def main():
    """"play game"""
    # only greet player on their first game
    game = input("Choose your game: O (Original) and T (Limited Tries)")
    while game.lower() not in ["o", "t"]:
        print("Invalid input, please enter O or T")
        game = input("Choose your game: O (Original) and T ( Limited Tries)")
    if game.lower() in ["t"]:
        num_tries()
    
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
    else:
        print("Thanks for playing!")
        # wanted to clear this out for new players
        scores.clear

def greet():
    """greet user"""
    name = input("Hello! What is your name? ")
    print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")
    return name
def num_tries():
    """"play game with a limit of tries"""
    greet()
    # this is checking for dificulty level and will determine number of tries
    answer = (input("Choose your diffuculty: 1(easy)-3(hardest)"))
    # checks for faulty input from user(not a number and number out of range)
    if answer.isdigit() is False:
        print("Numbers only yo")
        answer = (input("Choose your diffuculty: 0(easy) - 3(hardest)"))
    elif int(answer) > 3 or int(answer) < 1:
        print("Please choose between 1 - 3")
        answer = (input("Choose your diffuculty: 0(easy) - 3(hardest)"))
    else:
        # makes answer an int so I cann compare it for the next set of conditions
        answer = int(answer)
        
    if answer == 1:
        tries = random.randint(15,25)
    elif answer == 2:
        tries = random.randint(10,15)
    else:
        tries = random.randint(2,10)
    print (f"you have {tries} to guess the number. Good Luck!")
    
    # count number of tries
    counter = 1

    # randomizes number btw 1 and 100
    num = random.randint(1, 100)

    # call first user guess
    guess = validate_input()

    # check guesses
    while guess != num:
        tries -= 1
        if tries == 0:
            print("Oh no! You ran out of tries!")
            again = input("Play again? (if you want to go to main menu enter mm)")
            play_again(again)  
        counter += 1
        if guess > num:
            print("Your guess is too high, try again.")
            guess = validate_input()
        elif guess < num:
            print("Your guess is too low, try again.")
            guess = validate_input()

    # congratulate user for correct guess
    
    print(f"Well done! You found my number in {counter} tries!")

    # ask if user wants to play again
    again = input("Play again? ")
    play_again(again)

def play_again(text):
        """This calls function based on text given by user"""
        if text.lower() in ["yes", "y"]:
            num_tries()
        elif text.lower() in ["mm"]:
            main()
        else:
            print("Thanks for playing!")

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
