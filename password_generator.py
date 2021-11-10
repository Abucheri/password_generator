
import secrets
import string
alphabet = string.ascii_letters + string.punctuation  + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(15))  # for a 15-character password
print(password)
