"""Ask user for number, give hints about number if wrong"""

SECRET: int = 10
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing: 
    if guess == SECRET:
        print("Correct! You did it! Believe in your dreams!")
        playing = False
    else:
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even. ")
        if guess < SECRET:
            print("Guess was less than the answer. ")
        else: #guess is > SECRET:
            print("Guess was greater than the answer. ")
        guess = int(input("Wrong guess. Try again! "))