import secrets
import string

alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

combination = alphabets + numbers + symbols

length = 8

password = ''
for i in range(length):
    password += ''.join(secrets.choice(combination))

print(password)
