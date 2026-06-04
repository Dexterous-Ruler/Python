# name='harry'
# print(name[0])
# print(name[-1])

'''text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)
'''


# name="Harry0123456789"
# print(name[0:2])
# print(name[2:-1])
# print(name[0:10:2])
# print(name[0:10:3])

# text = "Python Programming"
# print(text[::2])   # Output: Pto rgamn
# print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)
# print(text[-6::-2]) # Output: ramin (negative indexing)

# text = "Welcome to Python!"
# print(text[:7])   # Output: Welcome
# print(text[-7:])  # Output: Python!
# print(text[3:-3]) # Output: come to Pyt


# s="hello world"
# a=len(s)
# print(a)
# print(s.upper())
# print(s.lower())
# print(s.capitalize()) 
# print(s.title())

# text="     \nhello    world  \n"
# print(text.strip())  # Output: "hello world" (removes leading and trailing whitespace)
# print(text.lstrip()) # Output: "hello world\n" (removes leading whitespace) 
# print(text.rstrip()) # Output: " \nhello world" (removes trailing whitespace) 

# text="python is fun"
# print(text.find("is"))  # Output: 7 (index of "is")
# print(text.find("fun")) # Output: 10 (index of "fun")
# print(text.find("Java")) # Output: -1 (not found)
# print(text.replace("fun", "awesome")) # Output: "python 

# text="apple, banana, cherry"
# print(text.split(", "))  # Output: ['apple', 'banana', 'cherry']
# print(text.split())     # Output: ['apple,', 'banana,', 'cherry'] (default split on whitespace)
# print(",".join(['apple', 'banana', 'cherry']))  # Output: apple, banana, cherry


# text="Python123"
# print(text.isalpha())  # Output: False (contains digits)
# print(text.isdigit())  # Output: False (contains letters)           
# print(text.isalnum())  # Output: True (contains only letters and digits)
# print(text.islower())  # Output: False (contains uppercase letters)
# print(text.isupper())  # Output: False (contains lowercase letters)
# print(text.isspace())  # Output: False (contains non-whitespace characters)

# text = "Hello, Python!"
# print(len(text))  # Output: 14

# print(ord('A'))  # Output: 65
# print(chr(65))   # Output: 'A'

# text = "apple,banana,orange"
# fruits = text.split(",")
# print(fruits)  # Output: ['apple', 'banana', 'orange']

# new_text = " - ".join(fruits)
# print(new_text)  # Output: "apple - banana - orange"

#string formatting
# template ="Dear {}, You are awesome. Take this {}$ bag"
# a="john"
# a1=10000
# b="jack"
# b1=1000
# c="Marie"
# c1=300

# s1=template.format(a,a1)
# print(s1)
# s2=template.format(b,b1)
# print(s2)

# print(f"{c} you are awesome and Take this {c1}$ bag")

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python
print("{name} is {age} years old".format(name="Bob", age=25))

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

text = "Python"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align

