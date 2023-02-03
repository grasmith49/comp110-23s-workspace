"""One Shot Wordle Exercise."""

__author__ = "730546449"

SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"

x: int = 0
boxes: str = ""
letter: bool = False 
alt_idx: int = 0

word: str = input(f"What is your {str(len(SECRET_WORD))}-letter guess? ")

while len(word) != len(SECRET_WORD):
    word = str(input(f"That was not {str(len(SECRET_WORD))} letters! Try again: "))

if len(word) == len(SECRET_WORD):
    if word == SECRET_WORD: 
        while x < len(SECRET_WORD):
            if word[x] == SECRET_WORD[x]:
                boxes = boxes + GREEN_BOX
            x = x + 1
        print(boxes)
        print("You got it!")
    else:
        alt_idx = 0
        while x < len(SECRET_WORD):
            if word[x] == SECRET_WORD[x]:
                boxes = boxes + GREEN_BOX
            else:    
                while alt_idx < len(SECRET_WORD) and letter is False:
                    if word[x] == SECRET_WORD[alt_idx]:
                        letter = True
                    else:
                        alt_idx = alt_idx + 1
                if letter is True:
                    boxes = boxes + YELLOW_BOX
                    letter = False
                    alt_idx = 0
                else: 
                    boxes = boxes + WHITE_BOX
                    alt_idx = 0
            x = x + 1
        print(boxes)
        print("Not quite. Play again soon!")