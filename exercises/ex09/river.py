"""File to define River class."""
 
__author__ = "730546449"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class simulates the life cycle of a river over a week involving fish and bears."""
    
    # attributes
    day: int  # tells you what day of the river's lifecycle you are modeling
    bears: list[Bear]  # stores the river's bear population
    fish: list[Fish]  # stores the river's fish population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears, if they are too old then it removes them from the population."""
        surviving_fish: list[Fish] = []
        survivng_bears: list[Bear] = []
        for x in self.fish:
            if x.age <= 3:
                surviving_fish.append(x)
        for y in self.bears:
            if y.age <= 5:
                survivng_bears.append(y)
        self.fish = surviving_fish
        self.bears = survivng_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes fish for the purposes of bears eating."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        """Simulates bears eating if there is a large enough fish population."""
        for x in self.bears:
            if len(self.fish) >= 5:
                x.eat(3)
                self.remove_fish(3)         
        return None
    
    def check_hunger(self):
        """Checks the hunger score of the bears, if the bears are starving then it removes them from the population."""
        surviving_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                surviving_bears.append(x)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """For every two fish, four fish are spawned."""
        fish_pop: int
        fish_pop = len(self.fish)
        while fish_pop >= 2:
            self.fish.append(Fish)
            self.fish.append(Fish)
            self.fish.append(Fish)
            self.fish.append(Fish)
            fish_pop -= 2
        return None
    
    def repopulate_bears(self):
        """For every two bears, one bear is spawned."""
        bear_pop: int
        bear_pop = len(self.bears)
        while bear_pop >= 2:
            self.bears.append(Bear)
            bear_pop -= 2
        return None
    
    def view_river(self):
        """Shows the day, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls the one_river_day function 7 times to simulate a week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
