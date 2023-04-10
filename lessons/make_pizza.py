"""Practice instantiating Pizza class"""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large")

my_pizza.toppings = 1
my_pizza.gluten_free = True

print(my_pizza.size)