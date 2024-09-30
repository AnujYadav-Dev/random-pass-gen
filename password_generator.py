import random
import string

def generate_password(length):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
try:
    length = int(input("Enter the desired length of the password: "))
    
    # Ensure the password length is reasonable
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
