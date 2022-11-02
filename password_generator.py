import random
import string

print('''
=============================''')
print("Welcome To Password Generator")
print('''=============================


''')


length = int(input("Please define your length of Password : "))

print('''Please select what you want on your password :
        1) Numbers
        2) Letters
        3) Special Symbol
        4) Exit
''')

characterList = ''

while True:
    choice = int(input("Pick a number : "))
    if choice == 1 :
        characterList += string.ascii_letters
    elif choice == 2:
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please enter a valid number !")
    
password = []


for i in range (length):
    random_pass = random.choice(characterList)

    password.append(random_pass)

print("The random password is " + "".join(password))