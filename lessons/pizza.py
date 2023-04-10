"""Define Pizza class"""

class Pizza:

    # attributes
    size: str # "small" or "large"
    toppings: int
    gluten_free: bool

def __init__(self, size_input: str):
    self.size = size_input