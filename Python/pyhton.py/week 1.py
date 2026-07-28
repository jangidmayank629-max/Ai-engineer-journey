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




#---------+

# 1. Even / Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Positive / Negative / Zero
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 3. Largest of 2 Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)


# 4. Largest of 3 Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


# 5. Leap Year
year = int(input("\nEnter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 6. Voting Eligibility
age = int(input("\nEnter your age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# 7. Pass / Fail
marks = float(input("\nEnter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 8. Grade Calculator
marks = float(input("\nEnter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")


# 9. Divisible by 5 and 11
num = int(input("\nEnter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 10. Simple Calculator
num1 = float(input("\nEnter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid Operator")

