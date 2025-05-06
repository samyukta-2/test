import random

def generate_number():
    """Generate a 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))
