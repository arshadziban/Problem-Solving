import random
import string

def generate_password(length=8):
    # Define the characters that can be used in the password
    characters = string.digits  # Only numbers
    
    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_password(12)  # Generate a 12-digit password
print("Generated Password:", password)
