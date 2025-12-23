# Comparasion Operators

# > greater than  >= greater than or equal to
# < less than  <= less than or equal to
#  == equality !=  not equal

print(ord("b"))  # this provides the ascii value

# ---------------------------------------------------------------
# Conditinal Statements
print("==============================================")
temperature = 35
if temperature > 30:
    print("It is a hot day ")
    print("It is warm day!!")

#   If we put two white spaces after if condition, python intrepretor undersatnds
#  that all the code below is after if statement. so if you have to end that exclude the two white spaces.
# pep8 will recommend 4 white spaces
print("This is not included in if statement either it is true or false")

# Another example:
print("==============================================")
price = 1000
price1 = 2000
if price > price1:
    print("This is printed when the if statement is true")
print("This line is printed outside the if statement")

print("==============================================")

# Multiple conditional statements
# =============================================
print("==============================================")
temp = 40
if temp < 20:
    print("Today is cold!")
elif temp > 40:  # short form of else if
    print("Today is very hot!!!")
else:
    print("Today is normal day!!!")
print("==============================================")

# ===================================================
# The entire code section will run because there are not any connditions!
# check practice.py file for a perfect example!

# -------------------------------------------------------------------
# ternary operator
print("==============================================")
age = 12
message = "Eligible for uni" if age >= 18 else "Not eligible"
print(message)
print("====================================================")

# Logical Operators
# and
# or
# not

# lets make a program to test if someone is eligible to loan or not using logical operator

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible")


print("==============================================")
# in and operator if both conditions are true, it will be true
#  in or opeirator if atleast of one condition is true, it will be true

high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible")


print("==============================================")

high_income = True
good_credit = True
student = False

if not student:
    print("Eligible for loan")
else:
    print("Not eligible")

# Not operator inverses the boolen value i.e. if true it will make false and if false it will make true
print("==============================================")

high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible")

print("==============================================")


# -------------------------------------------------------
# Short Cicuit Evaluation


high_income = True
good_credit = True
student = False

if high_income or good_credit and not student:
    print("Eligible for loan")
else:
    print("Not eligible")

print("==============================================")

# --------------------------------------------------------------
# Chaining comparasion operators

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# The above code also can be written as:
if 18 <= age < 65:  # this simply means if age is greater and equal to 18 and less than 65
    print("Eligible")

print("==============================================")
