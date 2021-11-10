# importing required libraries
import random  # used to create a random string for the password
import string  # The string module contains various string constant which contains the ASCII characters of all cases, It has separate constants for lowercase, uppercase letters, digits, and special symbols, which we use as a source to generate a random string.

# getting random password of length 15 using letters, digits, and symbols
# random.choice() function is used to select random characters.
# string.ascii_letters is used to include letters from a-z and A-Z
# string.digits is used to include digits from 1 to 10
# string.punctuation is used to get special symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(15))  # generates a password of 15 characters
print("Your password is:", password)
