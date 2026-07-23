#Basic (1–10)

# Hello World
print("Hello World")

# Print your name
print("Mayank jangid")

# Store age in a variable
Age = 19

# Add two numbers
Num1 = 4
Num2 = 5
print("Sum=:",Num1 + Num2)

# Subtract two numbers
print("Subtrct:", Num2 - Num1)

# Multiply two numbers
print("Multiplication:", Num1 * Num2)

# Divide two numbers
print("divide:", Age / Num1)

# Find remainder
print(19 % 4)

# Square of a number
print( "Square:", Num1 ** 2)

# Cube of a number
print("Cude:", Num2 **3 )

# Input Based (11–15)

# 11. Take name as input
Name = input("Enter your name")

# 12. Take age as input
Age = int(input("Enter your age: "))

# 13. Add two input numbers
num1 = int(input("Enter first number"))
num2 = int(input("input second number"))

print("Sum of these numbers is: ", num1+num2)

# 14. Area of rectangle
#area of rectangle = l*b
length = int(input("input length of rectangle"))
breadth = int(input("input breadth of rectangle"))

area = length * breadth

print("Area of this rectangle is: ",area)

# 15. Area of circle
#area or circle = pie*r**2
radius = int(input("input radius of the circle"))

area = 22/7 * (radius **2 )

print("Area of this circle: ", area)

# Calculation Based (16–20)

#  16. Celsius → Fahrenheit
# Fahrenheit = (celcius * 9/5)+32
celcius = (int(input("Enter celcius to change in fahrenheit")))

fahrenheit = (9/5*celcius)+32

print("fahrenheit: ",fahrenheit)

#  17. Swap two numbers
num1 = 5
num2 = 6

print("numbers before swap: ", num1,num2)

num1,num2 = num2,num1

print("numbers after swap :",num1,num2)

#  18. Simple Interest
#formula of simple intrest = (principle*rate*time)/100
principle = int(input("Enter the principle amount "))
rate = float(input( "Enter the  annual rate of intrest(%) "))
time = int(input("Enter time in years"))

total_intrest = ((principle*rate*time)/100)

print("Total intrest: ",total_intrest)

#  19. Average of 5 numbers
# average of 5 numbers (num1 + num2 + num3 + num4 + num5)/5
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))
num5 = int(input("Enter fifth number"))

avg = (num1 + num2 + num3 + num4 + num5)/5
print("Average of all 5 numbers: ",avg)


#  20. Percentage calculato
# formula of percentage = (obtained / total )*100(%)
obtained_marks = int(input("Enter marks obtained by you: "))
total_marks = int(input("Enter total marks "))

percentage = (obtained_marks / total_marks )*100
print("Total percentage you will get: =", percentage,"%")
