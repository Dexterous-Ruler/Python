# question 1
# Create a string variable name with your full name. Print:

# The first character
# The last character
# The length of the string

'''name = "John Doe"
print("First character:", name[0])  # Output: 'J'
print("Last character:", name[-1])  # Output: 'e'
print("Length of the string:", len(name))  # Output: 8

# Concatenate two strings: "Hello" and "World" with a space in between.
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(str1,str2)
print(result)  # Output: "Hello World"

# question 2
# Given text = "Python Programming", do the following:

# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
text = "Python Programming"
print("First 6 characters:", text[:6])  # Output: 'Python'
print("Last 6 characters:", text[-6:])  # Output: 'amming'
print("Every second character:", text[::2])  # Output: 'Pto rg

# Reverse the string text using slicing.
print("Reverse the string",text[::-1])  # Output: 'gnimmargorP nohtyP'

# question 3
# Take the string "  i love python programming  " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

text = "  i love python programming  "
print("Remove extra spaces:", text.strip())  # Output: 'i love python programming'
print("Convert to title case:", text.strip().title())  # Output: 'I Love Python Programming'
print("Count of 'o':", text.count("o"))  # Output: 3

# Check if the string "123abc" is alphanumeric./
s = "123abc"
print("Is alphanumeric?", s.isalnum())  # Output: True (contains only letters and digits)

# question 4
# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

# Do the same using f-strings.
name = "John"
age = 25
sentence_format = "My name is {} and I am {} years old.".format(name, age)
print(sentence_format) 

sentence_fstring = f"My name is {name} and I am {age} years old."
print(sentence_fstring)

# question 5
# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
sentence = "Coding in Python is fun"
new_sentence = sentence.replace("fun", "awesome")
print(new_sentence)  # Output: "Coding in Python is awesome"

# Find the index of the word "Python" in sentence.
index = sentence.find("Python")
print("Index of 'Python':", index)  # Output: 11

# Convert the entire sentence to uppercase and print it.
print(sentence.upper())  # Output: "CODING IN PYTHON IS FUN"'''

# question 6
# Write a program that counts how many vowels are in a given string.
'''text=input("enter the text : ")
count=0
vowels="aeiouAEIOU"
for char in text:
    if char in vowels:
        count+=1
print("number of vowels in the text is : ",count)'''

# question 7
# Take a user input string and check if it is a palindrome (same forwards and backwards).

# text = input("Enter a string: ")

# # Reverse the string
# rev = text[::-1]

# if text == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an armstrong number because 1^3 + 5^3 + 3^3 = 153. Write a program that checks if a given number is an armstrong number or not.

num = int(input("Enter a number: "))

# Store original number
original = num
sum = 0

# Count number of digits
digits = len(str(num))

# Calculate sum of digits raised to power of digits
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

# Check Armstrong condition
if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")