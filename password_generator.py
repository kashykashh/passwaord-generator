import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ!@#$%^&*()"

while 1:
    password_len = int(input("What length would you like your password to be: "))
    password_count = int(input("How many passwords would you like: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0,password_len):
            password_characters = random.choice(characters)
            password            = password + password_characters
        print("Here is your password: ", password)