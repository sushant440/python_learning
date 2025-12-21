# pylint: disable=invalid-name, missing-module-docstring

print("hello world")
PRICE = 10
print(PRICE)
A = 10
B = 20
print(A+B)
X = 200
Y = 10
print(X*Y)
students_count = 1000
course = "Python Programming"
print(len(course))
print(course[2])
print(course[0:4])
first = "sushant"
last = "aryal"
full = first+" "+last  # concatination
fulll = f"{first} {last}"  # newer way
print(full)
print(fulll)
print(course.upper())
print(course.lower())
laptop = "mi notebook pro"
print(laptop.title())
speaker = " asta wolf banger"
print(speaker.strip())  # removes white space
print(course.find("Py"))  # index of p will be printed
print(course.find("gramming"))  # index of g will be printed
print(course.replace("Pr", "ii"))
print("mi" in laptop)  # if exists return true
print("mi" in speaker)  # if does not exists returns false
print("babal"not in speaker)
# numbers

p = 1 # integer
q = 1.1  # float
cmplx = 2+3j
firstnum= 10
secondnum=3
print(firstnum+secondnum)
print(firstnum/secondnum) #return floating value result
print(firstnum//secondnum) # return integer value result
print(firstnum%secondnum)#modulus division
print(firstnum**secondnum) #exponent i.e 10 to the power 3
# Augmented assignment operator
firstnum+=300
print(firstnum)