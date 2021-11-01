# Day 3 Topics
# Conditional Statements
# Logical Operators
# Code Blocks and Scope

print("\n#########  if - else and conditional operators #########\n")

# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))

# if height >= 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('Sorry, you have to grow taller before you can ride.')

# Comparison operators
# >     Greater than
# <     Less than
# >=    Greater than or equal to
# <=    Less than or equal to
# ==    Equal to
# !=    Not equal to

print("\n#########  3.1 Challenge - Odd or even? #########\n")
# number = int(input('Which number do you want to check? '))
# module = number % 2
# if module == 1:
#     print('This is an odd number.')
# else:
#     print('This is an even number.')

print("\n#########  if - else nested conditional operators #########\n")
# height = int(input('What is your height in cm? '))

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         print('Please pay $5.')
#     elif age <= 18:
#         print('Please pay $7.')
#     else:
#         print('Please pay $12.')
# else:
#     print('Sorry, you have to grow taller before you can ride.')


print("\n#########  3.2 Challenge - BMI Calculator 2.0 #########\n")
# height = float(input('Enter your height in m: '))
# weight = float(input('Enter your weight in kg: '))
# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print(f'Your BMI is {bmi}. You are underweight.')
# elif bmi <= 25:
#     print(f'Your BMI is {bmi}. You have normal weight.')
# elif bmi <= 30:
#     print(f'Your BMI is {bmi}. You are overweight.')
# elif bmi <= 35:
#     print(f'Your BMI is {bmi}. You are obese.')
# else:
#     print(f'Your BMI is {bmi}. You are clinically obese.')

print("\n#########  3.3 Challenge - Leap year #########\n")
# year = int(input('Which year do you want to check? '))
# divisible_by_4 = year % 4
# divisible_by_100 = year % 100
# divisible_by_400 = year % 400

# if divisible_by_4 == 0:
#     if divisible_by_100 == 0:
#         if divisible_by_400 == 0:
#             print('Leap.')
#         else:
#             print('Not Leap.')
#     else:
#         print('Leap.')
# else:
#     print('Not Leap.')


print("\n#########  Multiple if conditions #########\n")
# height = int(input('What is your height in cm? '))

# bill = 0

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         bill = 5
#         print('Please pay $5.')
#     elif age <= 18:
#         bill = 7
#         print('Please pay $7.')
#     else:
#         bill = 12
#         print('Please pay $12.')
#     wants_photo = input('Do you want a photo? Y or N. ')
#     if wants_photo == 'Y':
#         # Add 3 dollars to the bill
#         bill += 3
    
#     print(f'Your final bill is ${bill}.')
# else:
#     print('Sorry, you have to grow taller before you can ride.')

print("\n#########  3.4 Challenge - Pizza Order #########\n")

# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M, or L? -> ')
# add_pepperoni = input('Do you want pepperoni? Y or N -> ')
# extra_cheese = input('Do you want extra cheese? Y or N -> ')

# total_bill = 0
# if size == 'S':
#     total_bill += 15
#     if add_pepperoni == 'Y':
#         total_bill += 2
# elif size == 'M':
#     total_bill += 20
#     if add_pepperoni == 'Y':
#         total_bill += 3
# elif size == 'L':
#     total_bill += 25
#     if add_pepperoni == 'Y':
#         total_bill += 3

# if extra_cheese == 'Y':
#     total_bill += 1

# print(f'Your final bill is: ${total_bill}')

print("\n#########  Logical Operators #########\n")

# height = int(input('What is your height in cm? '))

# bill = 0

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         bill = 5
#         print('Please pay $5.')
#     elif age <= 18:
#         bill = 7
#         print('Please pay $7.')
#     elif age >= 45 and age <= 55:
#         print('Your ticket is free.')
#     else:
#         bill = 12
#         print('Please pay $12.')
#     wants_photo = input('Do you want a photo? Y or N. ')
#     if wants_photo == 'Y':
#         # Add 3 dollars to the bill
#         bill += 3
    
#     print(f'Your final bill is ${bill}.')
# else:
#     print('Sorry, you have to grow taller before you can ride.')

print("\n#########  3.5 Challenge - Love Calculator #########\n")

# print('Welcome to the Love Calculator!')
# name1 = input('What is your name? \n')
# name2 = input('What is their name? \n')

# lowercase_names = name1.lower() + name2.lower()

# true_word_letters = lowercase_names.count('t') + lowercase_names.count('r') + lowercase_names.count('u') + lowercase_names.count('e')
# love_word_letters = lowercase_names.count('l') + lowercase_names.count('o') + lowercase_names.count('v') + lowercase_names.count('e')

# score = int(f'{true_word_letters}{love_word_letters}')

# if score < 10 or score > 90:
#     print(f'Your score is {score}, you go together like coke and mentos.')
# elif score >= 40 and score <= 50:
#     print(f'Your score is {score}, you are alright together.')
# else:
#     print(f'Your score is {score}.')

print("#######################")
print("##       THIRD       ##")
print("##      PROJECT      ##")
print("#######################\n")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
if choice1.lower() == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice2.lower() == 'swim':
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        if choice3.lower() == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3.lower() == 'yellow':
            print("You found the treasure! You Win!")
        elif choice3.lower() == 'blue':
            print("You enter a room of beasts. Game Over.")
        else: 
            print('You fell into a hole. Game Over.')
    else:
        print('You fell into a hole. Game Over.')
else: 
    print('You fell into a hole. Game Over.')