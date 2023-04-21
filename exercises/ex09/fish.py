"""File to define Fish class."""


class Fish:
    """Fissh class that initializes a fish and establishes what happens to it in a day."""

    # attributes
    age: int

    def __init__(self):
        """Initializes the new fish's age as 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Ages the fish by one day."""
        self.age += 1
        return None