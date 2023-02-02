"""One Shot Wordle Exercise"""

__author__ = "730546449"

secret_word: str = "python"
x: int = 0
boxes: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001f7E8"
word: str = input(f"What is your {str(len(secret_word))}-letter guess? ")
if len(word) == len(secret_word):
    if word == secret_word: 
        letter: bool = False
        alt_idx: int = 0
        while x < len(secret_word):
            if word[x] == secret_word[x]:
                boxes = boxes + green_box
            else:    
                while alt_idx < len(secret_word) and letter == False:
                    if word[x] == secret_word[alt_idx]:
                        letter = True
                    else:
                        alt_idx = alt_idx + 1
                if letter == True:
                    boxes = boxes + yellow_box
                else: 
                    boxes = boxes + white_box
            x = x + 1
        print(boxes)
        exit()
    else:
        letter: bool = False 
        alt_idx: int = 0
        while x < len(secret_word):
            if word[x] == secret_word[x]:
                boxes = boxes + green_box
            else:    
                while alt_idx < len(secret_word) and letter == False:
                    if word[x] == secret_word[alt_idx]:
                        letter = True
                    else:
                        alt_idx = alt_idx + 1
                if letter == True:
                    boxes = boxes + yellow_box
                else: 
                    boxes = boxes + white_box
            x = x + 1
        print(boxes)
        print("Not quite. Play again soon!")
        exit()
while len(word) != len(secret_word):
    word: str = input(f"That was not {str(len(secret_word))} letters! Try again: ")
if len(word) == len(secret_word):
    if word == secret_word:
        letter: bool = False 
        alt_idx: int = 0
        while x < len(secret_word):
            if word[x] == secret_word[x]:
                boxes = boxes + green_box
            else:    
                while alt_idx < len(secret_word) and letter == False:
                    if word[x] == secret_word[alt_idx]:
                        letter = True
                    else:
                        alt_idx = alt_idx + 1
                if letter == True:
                    boxes = boxes + yellow_box
                else: 
                    boxes = boxes + white_box
            x = x + 1
        print(boxes)
        exit()
    else:
        letter: bool = False 
        alt_idx: int = 0
        while x < len(secret_word):
            if word[x] == secret_word[x]:
                boxes = boxes + green_box
            else:    
                while alt_idx < len(secret_word) and letter == False:
                    if word[x] == secret_word[alt_idx]:
                        letter = True
                    else:
                        alt_idx = alt_idx + 1
                if letter == True:
                    boxes = boxes + yellow_box
                else: 
                    boxes = boxes + white_box
            x = x + 1
        print(boxes)
        print("Not quite. Play again soon!")
        exit()
