import random
import string

# Generates a random password of length num_characters
def create_password (num_characters):
    """Function that generates a random password"""

    # Possible characters that could be in the password.
    characters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "1234567890"
    "!@#$%^&*()?_")

    # Joins the characters together based on the number
    # inputted by the user
    password = ''.join(random.choice(characters) for _ in 
        range(num_characters))
    
    return password