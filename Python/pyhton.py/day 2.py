# Operators & Conditional Statements

# Basic (1–9)
num = int(input("enter your number "))

if num > 0:
    print("positive ")
elif num < 0:
    print("negative")
else:
    print("zero")

# Check even odd
num1 = int(input("enter your number"))
if num1 % 2 == 0:
    print("even")
else :
    print("odd")

# 3. Largest of Two Numbers
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

if num1>num2:
    print("num1 is greater")
elif num1<num2:
    print("num2 is greater")
else:
    print("both are equal")

# 4. Largest of Three Numbers
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if num1 <= num2 and num2 <= num3:
    print("num 3 is the greater")
elif num3 <= num2 and num2 <= num1:
    print("num1 is greater")
else:
    print("num 2 is greater")


# 6. Check Voting Eligibility
age = int(input("enter your age "))

if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote ")



# 7. Check Leap Year



# 8. Check Divisible by 5


# 9. Check Divisible by 3 and 5



# 10. Grade Calculator

