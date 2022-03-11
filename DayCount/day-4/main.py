# Randomization and lists
from os import stat
import random
from turtle import pos

from matplotlib.pyplot import sci

print("\n#########  Using the Random function  #########\n")

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

print("\n#########  4.1 Challenge - Head or Tails?  #########\n")

# value = random.randint(0,1)
# if value == 0:
#     print('Heads')
# elif value == 1:
#     print('Tails')

print("\n#########  Data Structure : LIST #########\n")
# # Data Structure : A way to organize and store data in Python.
# # list_name = [item1, item2, ..., itemN]

# states_of_america = ['Delaware', 'Pennsylvania', 'Dakota', 'Alabama', 'New Mexico']

# # Modifying an element in the list
# # list_name[element_index] = new value
# states_of_america[0] = 'Texas'

# # Adding an element at the end of the list
# states_of_america.append('California')

print("\n#########  4.2 Challenge - Random Person Picker  #########\n")

# names_string = input('Give me everybody\'s names, separated by a comma. ')
# names = names_string.split(', ')
# names_length = len(names)
# lucky_number = random.randint(0,names_length - 1)
# print(f'{names[lucky_number]} is paying for the meal today!')

print("\n#########  Index Errors and Nested Lists  #########\n")

# states_of_america = ['Delaware', 'Pennsylvania', 'Dakota', 'Alabama', 'New Mexico']
# print(f'Number of States: {len(states_of_america)}')
# try:
#     print(states_of_america[len(states_of_america)])
# except IndexError:
#     print('[ERROR] You selected an index greater than the number of elements.')

# fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

# # List of lists
# dirty_dozen = [fruits, vegetables]
# print(f'List of lists: {dirty_dozen}')

print("\n#########  4.3 Challenge - Treasure Map  #########\n")

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# second_position = int(position[0])
# first_position = int(position[1])

# map[first_position-1][second_position-1] = 'X'

# print(f'{first_position} {second_position}')
# print(f"{row1}\n{row2}\n{row3}")

print("#######################")
print("##      FOURTH       ##")
print("##      PROJECT      ##")
print("#######################\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')

choice = int(choice)

if choice >= 3 or choice < 0:
    print('Invalid option.')
else:
    options = [rock, paper, scissors]

    rand_option = random.randint(0, 2)

    print(f'{options[choice]}\nComputer chose:\n{options[rand_option]}')

    if choice == rand_option:
        print('It\'s a tie.')
    elif choice == 0 and rand_option == 1:
        print('You lose.')
    elif choice == 0 and rand_option == 2:
        print('You win.')
    elif choice == 1 and rand_option == 0:
        print('You win.')
    elif choice == 1 and rand_option == 2:
        print('You lose.')
    elif choice == 2 and rand_option == 0:
        print('You lose.')
    elif choice == 2 and rand_option == 1:
        print('You win.')

 