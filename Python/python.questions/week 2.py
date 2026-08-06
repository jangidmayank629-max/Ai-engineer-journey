# # for loops 

# #16-----------1
for i in range(16, 0, -1):
    print(i)

# #20-----------50  
for i in range(20, 51, 1): 
    print(i) 

# # -3 ---- -15
for i in range (-3,-16, -1):
    print(i)

# # table of any number 
a = int(input("Enter a number: "))
for i in range( a, (a*10)+1 , a):
    print(i)

# # printing a names letters
a = "ALPHABET"
for i in range(len(a)):
    print(a[i])



# Write a program to print all even numbers from 1 to 50 using a for loop.

for i in range(0, 51, 2):
    print(i)


# Write a program to print numbers from 1 to 100, but use continue to skip all numbers that are divisible by 5.
for i in range(1, 101): 
    if i %5 == 0:
        continue
        
    print(i)

# Write a program to print numbers from 1 to 50, and use break to stop the loop when the number reaches 30.

for i in range(1, 51):
    if i == 30:
        break
    print(i)


# Write a program to print all numbers from 1 to 100 that are not divisible by 3 using continue.

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)

x = int(input("Enter the starting number: "))
for i in range(x, 101):
    if i % 3 == 0:
        continue
    print(i)

# Write a program to take a number  from the user and search for its first divisor other than  and itself. Use break when the divisor is found.

for i in range(2, 101):
    if 100 % i == 0:
        print(i)
        break

    

# Write a program to print numbers from 1 to 100, but:
 # Skip multiples of 3 using continue
 # Stop completely when the number reaches 80 using break

for i in range (1, 101):
    if i % 3 == 0:
        continue
    elif i == 80:
        break
    print(i)

# Write a program that takes 10 numbers from the user. If the user enters 0, immediately stop taking numbers using break. Otherwise, print each number.

for i in range(10):
   n = int(input("Enter a number: "))
   if n == 0:
       break

   print(n)

# Write a program to find the first number between 1 and 100 that is divisible by both 9 and 2. Use break when you find it.

for i in range(1, 101):
    if i % 9 == 0 and i % 7 == 0:
        print(i)
        break


# Challenge: Write a program that prints all numbers from 1 to 100, but:
 # Skip numbers divisible by 2 using continue
 # Skip numbers divisible by 3 using continue
 # Stop the loop completely when the number reaches 75 using break

for i in range (100):
  if i % 3 == 0 or i % 2 == 0:
    continue
  if i >= 75:
    break
  print(i)

# while loop

# printing 1 to 30

a = 1
while a <= 30:
    print(a)
    a += 1

# 121 in 1 , 2 ,1  (palindrone or not )
a = 121
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a //= 10
if copy == rev:
    print("Palindrome")
else:
    print("Not Palindrome")



# mini number gussing game
import random

num = random.randint(1, 20)
tries = 0
guess = int(input("Guess a number between 1 and 20: "))

while True:

   if num == guess:
    tries += 1
    print("Congratulations! You guessed the number .")
    break
   
   elif guess < num:
    tries += 1
    print("Your guess is too low. Try again.")

   elif guess > num:
    tries += 1
    print("Your guess is too high. Try again.")
    
   else:
    print("Invalid input. Please enter a number between 1 and 20.")
    



    