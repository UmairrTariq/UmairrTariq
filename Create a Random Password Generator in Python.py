import random
import string

def generate_password(length):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Define the desired password length
password_length = 12 # You can change this to any length you prefer

# Generate and print the password
password = generate_password(password_length)
print(f"Generated Password: {password}")
