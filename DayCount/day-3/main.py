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