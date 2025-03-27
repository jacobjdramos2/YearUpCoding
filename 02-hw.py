# Exercise 1: Multi-Condition Decisions
# I will be using if, elif, and else statements to determine the users age. 

age = 25 # Change this value to test

if age < 13: # Check if user is under 13
    print("PG movies only.")
elif age > 13 and age < 17: # Check if user is between the age 13 and 17 exclusive
    print("PG-13 movies allowed.")
else: # Else case says that the users age is older than 17, so all movies are allowed
    print("All movies allowed")

# Exercise 2: Deicison Tree for Discounts
# I will be using seperate if statements to determine if the user is a student and/or older than 64, while applying their respective discounts.
# The final if statement will check if the user is both a student and older than 64, applying the higher discount if true. 
is_student = False # Only change to test
age = 70 # Only change to test

older_or_equal_65 = False # New variable added to remember if the user is older.

if is_student: # If the user is a student, they qualify for the 20% discount offer.
    print("20% discount applied.")

if age >= 65: # If the user is 65 or older, they qualify for the 15% discount offer.
    older_or_equal_65 = True
    print("15% discount applied.")

if is_student and older_or_equal_65: # If the user is both, only the 20% discount offer will be applied. 
    print("20% Discount Applied.")

# Exercise 3: Loan Approval System
# Use if statement to determine if the applicant is at least 18. Else will print a reminder saying they need to be 18.
# I will have an inner if statement comparing the income, credit score, and checking to see if the user is in debt. 
age = 30
income = 45000
credit_score = 710
has_debt = True

if age >= 18: # Outer statement checking if the user is 18.
    if has_debt: # If the user is in debt, they must have an income > 40000 AND credit score > 700
        if income > 40000 and credit_score > 700:
            print("Loan Approved.")
        else: 
            print("Loan disapproved.")
    else: # Otherwise, they can either have an income > 40000 OR a credit score > 700
        if income > 40000 or credit_score > 700:
            print("Loan approved.")
        else:
            print("Loan disapproved.")
else: # Does not go into inner statements since the user is not 18.
    print("You must be 18.")

# Exercise 4: Complex Weather Decision System
# I will be using if, elif, and else statements to determine if the temp is below 32F, between 32F and 50F, above 50F with a 70% humidity, or printing "Mild Weather" otherwise.
temperature = 55
humidity = 80

if temperature < 32: # Checking if temp is less than 32F
    print("Freezing warning.")
elif temperature > 32 and temperature < 50: # Checking if temp is between 32F and 50F
    print("Cold weather.")
elif temperature > 50 and humidity > 70: # Checking if temp is above 50F AND humidity is above 70%
    print("Warm but humid.")
else: # If none are fulfilled, print Mild Weather
    print("Mild weather.")

# Exercise 5: Advanced Multi-Step Bank Security System
is_employee = False
is_manager = False
is_customer = True
account_balance = 5000
security_alert = False

if not security_alert:
    if is_employee:
        print("Full access granted.")
    elif is_manager:
        print("Granted access to sensitive files.")
    elif is_customer and account_balance > 1000:
        print("Transactions allowed")
    else:
        print("Access Denied.")
else:
    print("Access Denied")
