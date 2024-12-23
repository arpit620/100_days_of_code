import random
import string

def generate_random_password(length=12):
    """
    Generate a random password with a given length.
    
    The password will include a mix of uppercase and lowercase letters, digits,
    and punctuation characters. It ensures at least two digits and two special
    characters in the password.
    
    Args:
    length (int): The length of the password to generate. Default is 12.
    
    Returns:
    str: A randomly generated password.
    
    Raises:
    ValueError: If the length is less than 4.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    digits = string.digits
    special_characters = string.punctuation
    letters = string.ascii_letters

    # Ensure at least two digits and two special characters
    password = [
        random.choice(digits) for _ in range(2)
    ] + [
        random.choice(special_characters) for _ in range(2)
    ] + [
        random.choice(letters + digits + special_characters) for _ in range(length - 4)
    ]
    

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

if __name__ == "__main__":
    print("Random Password:", generate_random_password())
    # print("Random Password:", generate_random_password())
