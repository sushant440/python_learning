# Let's practice multiple conditional statement to execute a program to decide if the user is eligible to
# take citiozenship and the user can vote or not!

print("Welcome User! Lets check whether you can vote or not!")
x = input("Input your age: ")
age = int(x)
if age < 16:
    print("You are not eligible to make citizenship and either vote")

elif age == 16:
    print("You are just eligible to make citizenship")

elif age < 18:
    print("If are a citizenship holder if you have made citizenship but you cannot cast vote! ")

else:
    print("You can vote!!!")


# the type conversion can have been done in another way also
#  age= int(input("Input your age: "))
