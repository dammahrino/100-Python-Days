# Data Types

# String
stringVar = "Hello"
print(stringVar[0]) # Subscripting

# Get the letter o printed
print(stringVar[4])

# Integer
integerVar = 123
print(integerVar + 2)

# Float
floatVar = 3.141592
print(floatVar + 0.01)

# Boolean
booleanValue = True

# To know the type of a variable, we can use _type_ function
print(type(booleanValue))

# To convert an Integer to a String, we use _str_ function
intValue = 5
strValue = str(intValue)
print("The value is " + strValue)

print("\n#########  2.1 Challenge - Int and Str #########\n")
# Read user input
# two_digit_number = input("Type a two digit number: ")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(first_digit + second_digit)

print("\n#########  2.2 Challenge - BMI Calculator #########\n")
# Read user input
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# bmi = float(weight) / float(height) ** 2
# print(int(bmi))

print("\n#########  Number manipulation and F Strings #########\n")
# To rounds numbers, we can use de _round_ function
print(round(8/3, 2))

# Also we can use float division to return an int directly with _//_
print(type(4/2))  # Returns <class 'float'> even if remainder is -0
print(type(8//3)) # Returns <class 'int'>

# An easier way to concatenate different types of values in a string without
# the need to add _str_ function, is using an f-string
# f-string requires to add an _f_ before the single or double quotes in the string
numValue = 0
floatValue = 1.8
boolValue = True

print(f'The values are: {numValue} {floatValue} {boolValue}')

print("\n#########  2.3 Challenge - Your Life in Weeks #########\n")

# age = input('What is your current age? ')
# remainderYears = 90 - int(age)
# remainderMonths = remainderYears * 12
# remainderWeeks = remainderYears * 52
# remainderDays = remainderYears * 365

# print(f'You have {remainderDays} days, {remainderWeeks} weeks and {remainderMonths} months left.')

print("#######################")
print("##      SECOND       ##")
print("##      PROJECT      ##")
print("#######################\n")

print('Welcome to the tip calculator.')
total = input('What was the total bill? $')
tip_percentage = input('What percentage tip would you like to give? 10, 12, or 15? ')
number_of_people = input('How many people to split the bill? ')

total_float = float(total)
tip_int = int(tip_percentage)
people_int = int(number_of_people)
total_with_tip = total_float * (1 +(tip_int/100))
individual_payment = round(total_with_tip / people_int, 2)
print(f'Each person should pay ${individual_payment}')