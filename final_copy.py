import random  # importing necessary modules

print('Eunique password generator')

length = 15 # length of the password(15)

custom = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-[]}{`=+"><?,.:;/\'|'  # custom parameters with numbers, letters and symbols

ran = random.sample(custom, length)  # using the randon library to generate random characters

password = "".join(ran)  # creating password

print('Your password: ', password)  # print password
