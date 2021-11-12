import random  # importing necessary modules

print("Eunique Password Generator")

# length of the password(15)
length = 15

# custom parameters
lower_cased = 'abcdefghijklmnopqrstuvwxyz'
upper_cased = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# chars="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
numbs = '0123456789'
symbols = '~!@#$%^&*()_+-[]}{`=+"><?,.:;/\'|'

# combining all the characters
all_chars = lower_cased + upper_cased + numbs + symbols

# using the randon library ti generate random characters
ran = random.sample(all_chars, length)

# creating password
password = "".join(ran)

# print password
print('Your password: ', password)

