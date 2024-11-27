# File: name_generator.py

import random

# Define medieval first names for men and women
FIRST_NAMES_MEN = [
    "Arthur", "Baldric", "Cedric", "Edgar", "Gareth", 
    "Harold", "Lancelot", "Percival", "Roland", "Theodore"
]

FIRST_NAMES_WOMEN = [
    "Adelaide", "Beatrice", "Cecily", "Eleanor", "Felicity", 
    "Gwendolyn", "Isolde", "Margery", "Rosalind", "Winifred"
]

# Define a generic pool of medieval last names
LAST_NAMES = [
    "Blackwood", "Dawnbreaker", "Evershade", "Hawthorne", "Ironwood",
    "Kingsley", "Lancaster", "Ravenwood", "Thornfield", "Winterbourne"
]

def generate_name(gender):
    """
    Generate a full name based on gender.
    - `gender` should be either "Male" or "Female".
    """
    if gender == "Male":
        first_name = random.choice(FIRST_NAMES_MEN)
    elif gender == "Female":
        first_name = random.choice(FIRST_NAMES_WOMEN)
    else:
        raise ValueError("Invalid gender. Must be 'Male' or 'Female'.")
    
    last_name = random.choice(LAST_NAMES)
    return f"{first_name} {last_name}"

# Example usage (can be tested directly in this file)
if __name__ == "__main__":
    print(generate_name("Male"))
    print(generate_name("Female"))
