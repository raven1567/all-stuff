tries = 3
number = 19
print("Welcome to THE NUMBER GAME")
print("You get three guesses to get the right number")

while(tries > 0):
    guess = input("Guess a number between 1 and 20(inclusive):")
    if not guess.isnumeric():
        print("Thats not a positive whole number, try again")
    else:
        guess = int(guess)
        if(guess > 20):
            print("That number is not between 1 and 20, try again")
            tries -=1
        else:
            if(guess < 1):
                print("That number is not between 1 and 20, try again")
                tries -=1
            else:
                if(guess != number):
                    print("Incorrect")
        if(tries == 0):
            print("Loser. You ran out of tries")
        if(guess == number):
            print("You Win!! You are smarter than I thought")
            break
