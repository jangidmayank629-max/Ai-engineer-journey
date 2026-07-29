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




# Q1. Take user's name and age and print introduction
name = input("Enter name: ")
age = int(input("Enter age: "))
print("My name is", name, "and my age is", age)



# Q2. Take two numbers and perform all operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)



# Q3. Check whether number is positive, negative or zero
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



# Q4. Find largest among three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(a, "is largest")
elif b > a and b > c:
    print(b, "is largest")
else:
    print(c, "is largest")



# Q5. Check voting eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")



# Q6. Print multiplication table
num = int(input("Enter number: "))

for i in range(1,11):
    print(num*i)



# Q7. Find sum of numbers from 1 to N
n = int(input("Enter N: "))

total = 0

for i in range(1,n+1):
    total += i

print("Sum:", total)



# Q8. Find factorial
n = int(input("Enter number: "))

fact = 1

for i in range(1,n+1):
    fact *= i

print("Factorial:", fact)



# Q9. Reverse a number
num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num//10

print("Reverse:", reverse)



# Q10. Check palindrome number
num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num//10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



# Q11. Count digits
num = int(input("Enter number: "))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)



# Q12. Sum of digits
num = int(input("Enter number: "))

sum_digit = 0

while num > 0:
    sum_digit += num % 10
    num //= 10

print("Sum of digits:", sum_digit)



# Q13. Print Fibonacci series
n = int(input("Enter terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a,b = b,a+b



# Q14. Prime number checker
num = int(input("Enter number: "))

prime = True

if num <= 1:
    prime = False
else:
    for i in range(2,num):
        if num%i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")



# Q15. Student Grade Calculator
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



# Q16. Pattern Printing
for i in range(1,6):
    print("*"*i)



# Q17. Even numbers between 1-100
for i in range(1,101):
    if i%2==0:
        print(i)



# Q18. Find largest digit in a number
num = int(input("Enter number: "))

largest = 0

while num > 0:
    digit = num%10
    
    if digit > largest:
        largest = digit
        
    num//=10

print("Largest digit:", largest)



# Q19. Count vowels in string
text = input("Enter string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)



# Q20. Simple calculator using conditions
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print("Invalid operator")



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




# Q1. Print numbers from 1 to 100

for i in range(1, 101):
    print(i)


# Q2. Print numbers from 100 to 1

for i in range(100, 0, -1):
    print(i)


# Q3. Print all even numbers from 1 to 100

for i in range(2, 101, 2):
    print(i)


# Q4. Print all odd numbers from 1 to 100

for i in range(1, 101, 2):
    print(i)


# Q5. Find the sum of first N natural numbers

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)


# Q6. Print the multiplication table of a number

num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Q7. Find the factorial of a number

num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


# Q8. Print Fibonacci series up to N terms

n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# Q9. Find the sum of digits of a number

num = int(input("Enter number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits =", total)


# Q10. Reverse a number

num = int(input("Enter number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reverse =", reverse)


# Q11. Count the number of digits in a number

num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits =", count)


# Q12. Check whether a number is Prime or Not

num = int(input("Enter number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Q13. Check whether a number is Palindrome or Not

num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



# Q14. Check whether a number is Armstrong or Not

num = int(input("Enter number: "))
original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# Q15. Find the largest digit in a number
num = int(input("Enter number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("Largest digit =", largest)

