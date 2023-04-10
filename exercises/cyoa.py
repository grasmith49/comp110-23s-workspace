"""EX06 - Choose Your Own Adventure."""
"""What snack are you?"""
__author__ = "730546449"


# emojis for decision 1
YELLOW: str = "\U0001F49B"
BLACK: str = "\U0001F5A4"


# emojis for decision 2
MORNING: str = "\U0001F305"
EVENING: str = "\U0001F30C"


# emojis for decision 3
TEA: str = "\U0001FAD6"
COFFEE: str = "\U00002615"


# emojis for decision 4
KEEP_PEACE: str = "\U0001F91D"
FIGHT: str = "\U0001F91C"


# emojis for decision 5
GO_OUT: str = "\U0001F483 \U0001F57A"
STAY_IN: str = "\U0001F6CC"    


# emojis for snack results
CANDY: str = "\U0001F36C"
COOKIE: str = "\U0001F36A"
FRUIT: str = "\U0001F34E"
POPCORN: str = "\U0001F37F"
PRETZEL: str = "\U0001F968"
SPICY_SNACK: str = "\U0001F336"


# general globals
points: int = 0
player: str


def main() -> None:
    """Main function of the quiz that includes all of the other function calls.""" 
    greet()
    # decision 1
    entry: str = input("First choose a color for your player icon or to exit the game: yellow, black, or exit: ")
    entry_procedure(entry)
    global points
    if points >= 5:
        print("Now it is time for you snack assignment based on your answers!")
        snack(points)
        print("That's all folks! Thanks for playing!")


def greet() -> None:
    """Greets the player with a randomized greeting, asks for the players name, introduces the quiz, explains how to go through and exit the quiz."""
    from random import randint
    greeting: int = randint(1, 2)
    if greeting == 1:
        print("Howdy!")
    if greeting == 2:
        print("Top of the morning to yah!")
    global player
    player = input("What is your name player? ")
    print(f"Welcome {player} to the 'What Snack Are You?' quiz!")
    print("To play: When prompted type out one of the options given in all lowercase lettters.")
    print("If you would like to exit the quiz, just type 'exit' at any question without any quotation marks.")


def entry_procedure(entry: str) -> None:
    """Procedure that allows the player to enter the quiz."""
    while entry != "exit" and entry != "yellow" and entry != "black":
        entry = input("That was not yellow, black or exit. Try again: ")
    if entry == "exit":
        global player
        global points
        print(f"Thank you for playing {player}. You accumulated {points} points while playing. Goodbye!")
        points = 0
    if entry == "yellow":
        add_2(points)
        print(f"{player} likes the color yellow{YELLOW}!")
        # decision 2
        if points > 0:
            time: str = input("Choose your favorite time of day, morning or evening: ")
            time_quest(time)
            if points > 0:
                # decision 3
                drink: str = input("Do you prefer tea or coffee? ")
                drink_quest(drink)
                if points > 0:
                    # decision 4
                    conflict: str = input("When facing conflict do you keep peace or fight? ")
                    conflict_quest(conflict)
                    if points > 0:    
                        # decision 5
                        friday_night: str = input("On a friday night are you more likely to go out or stay in? ")
                        friday_night_quest(friday_night)        
    if entry == "black":
        add_1(points)
        print(f"{player} likes the color black{BLACK}!")
        # decision 2
        if points > 0:
            time: str = input("Chose your favorite time of day, morning or evening: ")
            time_quest(time)
            if points > 0:
                # decision 3
                drink: str = input("Do you prefer tea or coffee? ")
                drink_quest(drink)
                if points > 0:
                    # decision 4
                    conflict: str = input("When facing conflict do you keep peace or fight? ")
                    conflict_quest(conflict)
                    if points > 0:    
                        # decision 5
                        friday_night: str = input("On a friday night are you more likely to go out or stay in? ")
                        friday_night_quest(friday_night)


def add_1(pts: int) -> int:
    """A function that adds 1 point to total point count."""
    global points
    pts = points
    pts += 1
    points = pts
    return points


def add_2(pts: int) -> int:
    """A function that adds 2 points to total point count."""
    global points
    pts = points
    pts += 2
    points = pts
    return points


def time_quest(time: str) -> int:
    """Uses preference for morning or night to assigns them different string outputs (with emojis) and points depending on their choice. If else exits quiz."""
    from random import randint
    while time != "exit" and time != "morning" and time != "evening":
        time = input("That was not morning, evening or exit. Try again: ")
    if time == "exit":
        global player
        global points
        print(f"Thank you for playing {player}. You accumulated {points} points while playing. Goodbye!")
        points = 0
    if time == "morning":
        add_2(points)
        response: int = randint(1, 2)
        if response == 1:
            print(f"{player} prefers the morning{MORNING}!")
        if response == 2:
            print(f"{player} does not prefer the evening{EVENING}!")
    if time == "evening":
        add_1(points)
        response: int = randint(1, 2)
        if response == 1:
            print(f"{player} prefers the evening{EVENING}!")
        if response == 2:
            print(f"{player} does not prefer the morning{MORNING}!")
    return points


def drink_quest(drink: str) -> int:
    """Uses preference for coffee or tea to assigns them different string outputs (with emojis) and points depending on their choice. If else exits quiz."""
    while drink != "exit" and drink != "coffee" and drink != "tea":
        drink = input("That was not coffee, tea or exit. Try again: ")
    if drink == "exit":
        global player
        global points
        print(f"Thank you for playing {player}. You accumulated {points} points while playing. Goodbye!")
        points = 0
    if drink == "coffee":
        add_2(points)
        print(f"{player} likes to drink coffee{COFFEE}!")
    if drink == "tea":
        add_1(points)
        print(f"{player} likes to drink tea{TEA}!")
    return points
     

def conflict_quest(conflict: str) -> int:
    """Uses preference for keeping peace or conflict to assigns them different string outputs (with emojis) and points depending on their choice. If else exits quiz."""
    while conflict != "exit" and conflict != "keep peace" and conflict != "fight":
        conflict = input("That was not keep peace, fight or exit. Try again: ")
    if conflict == "exit":
        global player
        global points
        print(f"Thank you for playing {player}. You accumulated {points} points while playing. Goodbye!")
        points = 0
    if conflict == "keep peace":
        add_2(points)
        print(f"In times of conflict, {player} will keep peace{KEEP_PEACE}!")
    if conflict == "fight":
        add_1(points)
        print(f"In times of conflict, {player} will fight{FIGHT}!")
    return points


def friday_night_quest(friday_night: str) -> int:
    """Uses preference for going out or staying in to assigns them different string outputs (with emojis) and points depending on their choice. If else exits quiz."""
    while friday_night != "exit" and friday_night != "go out" and friday_night != "stay in":
        friday_night = input("That was not go out, stay in or exit. Try again: ")
    if friday_night == "exit":
        global player
        global points
        print(f"Thank you for playing {player}. You accumulated {points} points while playing. Goodbye!")
        points = 0
    if friday_night == "go out":
        add_2(points)
        print(f"On a friday night, {player} likes to go out{GO_OUT}!")
    if friday_night == "stay in":
        add_1(points)
        print(f"On a friday night, {player} likes to stay in{STAY_IN}!")
    return points


def snack(end_points: int) -> None:
    """Using the points the player has accrued throughout the quiz, it matches them with a snack emoji and description."""
    global points
    end_points = points
    if end_points == 5:
        print(f"Your snack is candy{CANDY}! This means that you are super sweet and full of energy! You know how to light up a room!")
    if end_points == 6: 
        print(f"Your snack is cookies{COOKIE}! This means that you are sweet and full of fun surprises!")
    if end_points == 7:
        print(f"Your snack is fruit{FRUIT}! This means that you are honest and wholesome!")
    if end_points == 8:
        print(f"Your snack is popcorn{POPCORN}! This means that you are super fun and full of pizzazz, you can be salty or sweet!")
    if end_points == 9:
        print(f"Your snack is pretzel{PRETZEL}! This means that you are flexible and adaptable! Although you are on the saltier side, you are complimented well with your sweeter counterparts!")
    if end_points == 10:
        print(f"Your snack is a spicy snack{SPICY_SNACK}! This means that you are firey, bold, and opinionated!")


if __name__ == "__main__":
    main()