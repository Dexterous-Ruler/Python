#Write a function greet() that prints "Hello, Python Learner!" when called.
def greet():
    print("Hello, Python Learner!")
greet()  # Call the function to see the output

#Write a function square(num) that returns the square of a given number. Test it with different numbers.
def square(num):
    return num * num
print(square(4))  # Output: 16
print(square(5))  # Output: 25  
print(square(10)) # Output: 100

#Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
def full_name(first, last):
    return f"{first} {last}"
print(full_name("John", "Doe"))  # Output: John Doe
print(full_name("Jane", "Smith"))  # Output: Jane Smith

#Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)
def calculate_area(length, width=10):
    return length * width
# Test with both length and width

print(calculate_area(5, 8))  # Output: 40
# Test with only length (use default width)
print(calculate_area(5))  # Output: 50 (5 * 10)

#Write a lambda function that adds two numbers and test it.
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
print(add(10, 20))  # Output: 30

#Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9,16, 25]

#Write a recursive function factorial(n) that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

#Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_of_digits(456))  # Output: 15 (4 + 5 + 6)



# Import the math module and use it to:

# Find the square root of 144
# Calculate sin(90°) (hint: use math.radians())

import math
# Find the square root of 144
sqrt_144 = math.sqrt(144)
print(sqrt_144)  # Output: 12.0
# Calculate sin(90°)
sin_90 = math.sin(math.radians(90))
print(sin_90)  # Output: 1.0

#Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
import requests
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Data fetched successfully!")
    print(response.json())  # Print the JSON response from the API      
else:
    print("Failed to fetch data. Status code:", response.status_code)


# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls./
def increment():
    counter = 0  # Local variable initialized to 0
    counter += 1  # Increment the counter by 1
    print(counter)  # Print the current value of counter
# Call the function multiple times to observe the behavior
increment()  # Output: 1
increment()  # Output: 1 (counter resets to 0 each time)

# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    a (int or float): The first number to multiply.
    b (int or float): The second number to multiply.
    
    Returns:
    int or float: The product of a and b.
    """
    return a * b
# Display the docstring using help()
help(multiply)

#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=' ')
        fibonacci(n - 1, b, a + b)
# Print the first 10 Fibonacci numbers
fibonacci(10)  # Output: 0 1 1 2 3 5 8 13 21 34 

#Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
# my_utils4.py

def is_even(n):
    return n % 2 == 0

# main.py
from my_utils4 import is_even
# Test the is_even function
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
