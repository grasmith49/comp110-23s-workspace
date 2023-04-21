"""File to define Bear class."""


class Bear:
    """Bear class that initializes a bear, establishes what happens to it in a day, and how the bear eats."""
    
    # attributes
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the age and hunger score of a new bear in the population."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Ages the bear by a day and deducts one point from its hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Establishes that the bear's hunger score is the same as the number of fish given, which simulates it eating."""
        self.hunger_score = num_fish
        return None