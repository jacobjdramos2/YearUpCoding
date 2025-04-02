# Basic List Operations
# First I am going to create a ordered list of integers (ascending).
# To display the original list, I am going to loop through the list and print each element.
# To change the second element, I will assign a new integer to index 1 of list. 
# Using append() method to add new element to end of list.
# Using pop(index) to remove an element from a specific index of list.

# Create List
list = [1,2,3,4,5]

# For each index in list, print each element
for element in list:
    print(element)

# Assign new element to index 1
list[1] = 9000

# Appending new element to the end of the list
list.append(10)

# Removing element on index 2
list.pop(2)

# Exercise 2: Membership Check
# First I am going to initialize a list of strings containing 5 colors.
# Use if statement to check if the color blue is in my list. If true print confirmation message, if false print confirmation message.

# Initialize list
list_colors = ["pink", "yellow", "red", "blue", "green"]

contains_blue = False

# Loop through list. For each element, check if current index contains "blue".
for color in list_colors:
    if color == "blue":
        contains_blue = True

# Based on boolean variable, check if my list contains blue and print confirmation.
if contains_blue:
    print("You have the color blue in your list!")
else:
    print("You do not have the color blue in your list.")

# Exercise 3: Real-World List Modification
# First I am going to create a list of 5 numbers.
# Then check if the third element is less than 50. If true, set that element to 50.
# Use the + operator to calculate the sum of first and last element. If sum is greater than 100, set last element to 0.
# Swap the first element with the third element by using simultaneous assignment.
# Loop through each index of list and print each element.

# Initialize list
numbers = [10,20,30,40,50,60,70,80,90,100]

# Check if third element is less than 50
if numbers[2] < 50:
    # If true, set element to 50.
    numbers[2] = 50

# Referencing first and last element of list
sum_SL = numbers[0] + numbers[-1]

# If sum is greater than 100, set last to 0
if sum_SL > 100:
    numbers[-1] = 0

# Swapping first and third element in list
numbers[0], numbers[2] = numbers[2], numbers[0]

# Loop through list and print each element
for num in numbers:
    print(num)

