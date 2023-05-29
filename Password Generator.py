import secrets
import string
import pyperclip

# define the length of the password
length = 12

# create a list of characters to randomly select from
alphabet = string.ascii_letters + string.digits + string.punctuation

# generate a random password using the secrets module
password = ''.join(secrets.choice(alphabet) for i in range(length))

# print the password to the console
print('Your random password is:, password')

# copy the password to the clipboard
pyperclip.copy(password)
print('Password copied to clipboard!')