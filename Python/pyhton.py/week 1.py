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




# Operators & Conditional Statements

# Basic (1–10)

# 1. Check Positive, Negative or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


# 2. Check Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 3. Largest of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")


# 4. Smallest of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    print(num1, "is smaller")
else:
    print(num2, "is smaller")


# 5. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


# 6. Check Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")


# 7. Check Leap Year
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# 8. Check Divisible by 5
num = int(input("Enter number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# 9. Check Divisible by 3 and 5
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not Divisible by both")


# 10. Grade Calculator
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# Intermediate (11–15)

# 11. Check Vowel or Consonant
ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


# 12. Check Alphabet, Digit or Special Character
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")


# 13. Absolute Value
num = int(input("Enter a number: "))

if num < 0:
    print(-num)
else:
    print(num)


# 14. Check Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 15. Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# Advanced (16–20)

# 16. Discount Calculator
amount = float(input("Enter purchase amount: "))

if amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

print("Final Amount:", amount - discount)


# 17. Electricity Bill Calculator
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill:", bill)


# 18. BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# 19. Simple Calculator using if-elif
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")


# 20. ATM PIN Verification
pin = input("Enter ATM PIN: ")

if pin == "1234":
    print("Access Granted")
else:
    print("Wrong PIN")
```
