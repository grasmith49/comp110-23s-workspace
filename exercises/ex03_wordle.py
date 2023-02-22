"""Structured Wordle."""

__author__ = "730546449"


def contains_char(word: str, char_searched: str) -> bool:
    """With two strings (the first is of any length, the second is one character), return True if the second string is in the first and return False if it is not."""
    assert len(char_searched) == 1
    x: int = 0
    while x < len(word):
        if word[x] == char_searched:
            return True
        else:
            x = x + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Returning a string of emojies whose color codifies the indicies of the guess word as in the secret word and correct placement, in the secret word and wrong placement, or not in the secret word."""
    assert len(guess) == len(secret)
    x: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001f7E8"
    boxes: str = ""
    #If the guessed word and the secret word are the same, it prints out a string of green boxes for each index.
    while x < len(secret):
        if guess[x] == secret[x]:
            boxes = boxes + GREEN_BOX
        else: 
            if contains_char(secret, guess[x]) is True:
                boxes = boxes + YELLOW_BOX
            else:
                boxes = boxes + WHITE_BOX
        x = x + 1
    return boxes

def input_guess(input_word: int) -> str:
    """Checks to see if the inputted guess is the same length as the secret word."""
    first_try: str = input(f"Enter a {input_word} character word: ")
    while len(first_try) != input_word:
        first_try = input(f"That wasn't {input_word} chars! Try again: ")
    return first_try
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 6
    current_turn: int = 0
    guess: str = ""
    #While loop that checks if you still have available turns and have not won yet.
    while current_turn < turns:
        current_turn = current_turn + 1
        print(f"=== Turn {current_turn}/{turns} ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        #If the guess is correct, then you win and the following message is presented.
        if guess == secret_word:
            print(f"You won in {current_turn}/{turns} turns!")
            current_turn = 6
    #If you use all of your turns and lose, then it presents the following message.
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()