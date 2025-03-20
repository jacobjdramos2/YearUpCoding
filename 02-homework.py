# Excerise 1: Variables
# 1. Determine the cost of some number of pounds of cement. Assume there is a sales tax that applies

# Lbs of Cement 
lbs_pounds = 94

# Cost for this much cement in lbs
cost = 18.00

# Sales Tax
sales_tax = .725

def calculate_total_cost(lbs, cost, sales_tax):
    # Get the tax by multiplying the cost to the sale_tax
    tax = cost * sales_tax

    # The toal cost is the sum of the total cost and tax, then round to 2nd decimal point
    total_cost = round(cost + tax,2)

    print("The total cost is: ", total_cost, " for ", lbs, " lbs!")

calculate_total_cost(lbs_pounds, cost, sales_tax)

# 2. Given the cost of various containers of eggs (perhaps half a dozen, and 1 1/2 dozen), determine the cost per egg for each of those containers.
# Type of egg container
half_dozen = 6
one_half_dozen = 18

# Calculating the price per egg
def price_per_egg(half_dozen, one_half_dozen):
    # Storing key information
    half_dozen_price = 1.80
    one_half_dozen_price = 5.40

    # Divide the price to the number of eggs in the container, then round it to the 2nd decimal using round()
    per_egg_halfdozen = round(half_dozen_price/half_dozen,2)
    per_egg_onehalfdozen = round(one_half_dozen_price/one_half_dozen,2)

    print("Price per egg for a half dozen is: ", per_egg_halfdozen, "\nPrice per egg for one half dozen is ", per_egg_onehalfdozen)

price_per_egg(half_dozen, one_half_dozen)  

# 3. Given an hourly wage and the number of hours worked, determine how much a worker should be paid for shoveling snow. 
# First store the hourly wage and number of hours worked that day
hourly_wage = 15
hours_worked = 4

# Get how much a worker should be paid that day by multiplying the hourly wage to the hours worked
def paid(hourly_wage, hours_worked):
    paid = hourly_wage * hours_worked

    print("You got paid ", paid," dollars!")

paid(hourly_wage, hours_worked)

# Exercise 2: Boolean Expressions
# 1. Given the number of hours worked in a week, determine whether the employee will receive any overtime pay.
# Assigning the number of hours to determine the worker qualifying for overtime pay

def qualify_overtime_pay(hours_week):
    # Boolean statement that sends true if worker qualifies, false if not. 54 hours a week is the required pay
    return hours_week >= 54

yes_overtime_pay = 54
print(qualify_overtime_pay(yes_overtime_pay))
no_overtime_pay = 2
print(qualify_overtime_pay(no_overtime_pay))

# 2. Determine whether someone else's name is the same as your name.
someone_name = "Hamilton"
someone_name_same = "Jacob"
my_name = "Jacob"

# False case
print(someone_name == my_name)
# True case 
print(someone_name_same == my_name)

# 3. Determine whether the number of consecutive days of rain is at least 3.
# For the sake of the lesson I am assigning 3 to this variable 
at_least_three = 3

# True 
yes_three_rainy = 5
print(yes_three_rainy >= at_least_three)

# True
yaaa_three_rainy = 3
print(yaaa_three_rainy >= at_least_three)

# False 
no_three_rainy = 2
print(no_three_rainy >= at_least_three)

# Exercise 3: Pseudocode
# 1. Output a warning if the person's name is empty
name = input("Enter name: ")

# If the input string is blank, warning is displayed.
if name == "":
    print("WARNING! Name cannot be empty.")

# 2. Turn on the fuel warning light when the number of gallons remaining is less than 1.5.
# Gallons
gallon_warning = 1
gallon_no_warning = 1.5
gallon_no_warning2 = 2

# If number of gallon is less than 1.5 print warning light on, if not print no warning light.
def warning_light(gallons):
    if (gallons < 1.5):
        print("Fuel Warning Light is On!")
    else:
        print("No Fuel Warning Light.")

# Function call for testing
warning_light(gallon_warning)
warning_light(gallon_no_warning)
warning_light(gallon_no_warning2)

# 3. BMI can be calculated as 703 times weight in pounds, divided by the height in inches squared. Output "Healthy BMI" is the calculated BMI is below 25.
# Asking user to give me their weight and height
weight = input("Give me your weight: ")
height_in = input("Give me your height in inches: ")

# To calculate their BMI, I multiply weight by 703, height squared, then divide the two products
def bmi_calculator(weight, height):
    # Convert string to int data type in order to perform calculations
    weight = int(weight)
    height = int(height)
    bmi = (703*weight) / (height ** 2)
    # If their BMI is under 25 they are healthy, if their bmi is equal to 25 or higher, then their BMI is above average and considered not healthy
    if bmi < 25:
        print("You have healthy BMI!")
    else:
        print("Your BMI is above average :(")

bmi_calculator(weight,height_in)

# Exercise 4: If Statements
# Explain what each if statements is doing/asking

# Assigning int values to variables called feet and inches 
feet = 4
inches = 8

# If feet times 12 plus the amount of inches (8) is greater than or equal to 56, print ...
if feet * 12 + inches >= 56:
    print('...')

# Assigning int values to variables called hours and days
hours = 220
days = 0

# If hours (220) is greater than 23, assign days with hours // (floor division) 24. Then print the days
# The next line, days is multiplied by 24, and the product is subtracted from the hours.
if hours > 23:
    days = hours // 24
    print(days)
    
print(hours - days * 24)

# Assigning int value to variable eggs
eggs = 45

# If eggs is greater than or equal to 12, print the dividend of the amount of eggs and 12, representing how many dozen eggs. Note that '//' is floor division and
# only cares about the integer portion
if eggs >= 12:
    print(eggs // 12, 'dozen')

# This line does the expression in the parenthesis first, the dividend is multiplied by 12, and eggs is subtracted by the product. Then prints plus (difference).
print('plus', eggs - (eggs // 12) * 12)

# Ask user how much they would like in their party.
# Ask user what start time of the movie they want to see.
# Ask user how many people in party is 62 years old or older.
# Ask user how many students are in party.
# If their desired time is after 4:30pm charge them $10, or $7.50 if before 4:30pm
# give students a 25% discount on ticket price
# If party has over 10 people, minus $1 for every person on top of any other discounts

# Setting price to 0 and before and after 430 to false temporarily
price = 0
before_430 = False
after_430 = False

# Asking how many people watching and convert the string to int 
num_in_party = input("How many of you are watching?: ")
num_in_party = int(num_in_party)

# Looping just in case the user doesn't give me what I want, once they give me an answer I convert the String to an int
while (True):
    desired_time = input("What time would you like to watch? (Pick a number from 1-12): ")
    desired_time = int(desired_time)
    if (desired_time < 1 or desired_time > 12):
        print("This is not an option! Pick a number from 1-12!") 
    else:
        desired_time = int(desired_time)
        break

# If desired time is before 4.5 they are paying for before 430, else means they are payng for after 430 price
if (desired_time < 4.5):
    before_430 = True
else:
    after_430 = True

if (before_430):
    price = num_in_party * 10

if (after_430):
    price = float(num_in_party) * 7.50

# Now calculating discounts: First get number of seniors and convert string to int
senior_discount = 0
num_62_or_older = input("How many of you are 62+?: ")
num_62_or_older = int(num_62_or_older)

# To get the discount, I am multiplying the number of seniors and individual price and dividing the product by 2 to ensure 50% discount. Then subtracting that 
# difference to the total price.
if (before_430):
    senior_discount = (num_62_or_older * 10)/2
    price = price - senior_discount

if (after_430):
    senior_discount = float(num_62_or_older * 7.50)/2
    price = float(price) - senior_discount

# Same calculations here, except I am basing it off of the the number of students and using student discount variable. 
student_discount = 0
num_students = input("How many of you are students?: ")
num_students = int(num_students)

if (before_430):
    student_discount = float(num_62_or_older * 7.50)/4
    price = float(price) - student_discount

if (after_430):
    student_discount = float(num_62_or_older * 7.50)/4
    price = float(price) - student_discount

# To calculate this discount, I am using this if statement and subtracting the number in party to the price to ensure the $1 discount
if (num_in_party >= 10):
    price = price - float(num_in_party)

