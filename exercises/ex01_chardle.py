"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730546449"

word: str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters.")
    exit()
if len(word) < 5:
    print("Error: Word must contain 5 characters.")
    exit()
character: str = input("Enter a single character: ")
if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)
x: int = 0 
if word[0] == character:
    print(character + " found at index 0.") 
    x = x + 1
if word[1] == character:
    print(character + " found at index 1.")
    x = x + 1
if word[2] == character:
    print(character + " found at index 2.")
    x = x + 1
if word[3] == character:
    print(character + " found at index 3.")
    x = x + 1
if word[4] == character:
    print(character + " found at index 4.")
    x = x + 1
if x > 1:
    print(str(x) + " instances of " + character + " found in " + word)
if x == 1:
    print("1 instance of " + character + " found in " + word)
if x == 0:
    print(character + " not found.")
    print("No instances of " + character + " found in " + word)