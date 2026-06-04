#Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
'''number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))
if age >= 18:   
    print("You are eligible to vote.")
else:   
    print("You are not eligible to vote.")

#Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
day_number = int(input("Enter a day number (1-7): "))
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")'''

#Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation=input("enter the operation : ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of the following: +, -, *, /.")'''

#Print numbers from 1 to 10 using a for loop.
'''for i in range(1, 11):
    print(i)

#Print the multiplication table of a number (entered by user).
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

#Calculate the sum of all numbers from 1 to 100 using a for loop.
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(f"The sum of all numbers from 1 to 100 is: {total_sum}")'''


#Print the following pattern using a for loop:

'''for i in range (1, 5):
    print("* " * i)'''

#Print numbers from 1 to 10 using a while loop
'''i=1
while i<=10:
    print(i)
    i+=1

#Write a program that keeps asking the user to enter a password until they enter the correct one.
correct_password = "password123"
while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")'''


#Use a while loop to reverse a given number (e.g., 123 → 321).

'''number = int(input("Enter a number: "))
reversed_number = 0 
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10
print(f"The reversed number is: {reversed_number}")'''

#Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
for i in range(1, 11):
    if i == 7:
        break
    print(i)

#Use a for loop to print numbers from 1 to 10, but skip the number 5 (use continue).
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

for i in range(1,6):
    if i==3:
        pass
    print(i)