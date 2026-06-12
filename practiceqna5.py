# Create a list fruits = ["apple", "banana", "cherry"].

# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
print(len(fruits))  # Output: 3


# Create a list of numbers from 1 to 10.

# Print the first three numbers using slicing.
# Print the last three numbers using slicing.

numbers = list(range(1, 11))
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[-3:])  # Output: [8, 9, 10]

list1=[i for i in range(1,11)]
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[0:3])  # Output: [1, 2, 3]
print(list1[-3:])  # Output: [8, 9, 10] 

# Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 7, 9]
numbers.append(10)
print(numbers)  # Output: [1, 2, 5, 7, 9, 10]
numbers.remove(2)
print(numbers)  # Output: [1, 5, 7, 9, 10]  



# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)  # Output: ['Alice', 'David', 'Bob', 'Charlie']

# Create a tuple coordinates = (10, 20) and print both elements.
coordinates = (10, 20)
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
'coordinates[0] = 50  # This will raise a TypeError because tuples are immutable'

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
coordinates_list = list(coordinates)
coordinates_list[0] = 50
print(coordinates_list)  # Output: [50, 20]
coordinates = tuple(coordinates_list)
print(coordinates)  # Output: (50, 20)

# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4} (duplicate 3 is removed)

# Add 5 to the set, remove 2, and check if 4 is in the set./
my_set.add(5)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}
print(4 in my_set)  # Output: True



# Create two sets:

# a = {1, 2, 3}

# b = {3, 4, 5}
# Find their:

# Union

# Intersection

# Difference (a - b)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))       # Output: {1, 2, 3, 4, 5}
print(a.intersection(b))  # Output: {3}
print(a.difference(b))   # Output: {1, 2}

# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:

# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".


student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])  # Output: John
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A+', 'city': 'Delhi'}

# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

friends = {"Alice": "123-456-7890", "Bob": "234-567-8901", "Charlie": "345-678-9012"}
print(friends.keys())    # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print(friends.values())  # Output: dict_values(['123-456-7890', '234-567-8901', '345-678-9012'])
print(friends.items())   # Output: dict_items([('Alice', '123-456-7890'), ('Bob', '234-567-8901'), ('Charlie', '345-678-9012')])
for key, value in friends.items():
    print(f"{key}: {value}")

# Write a program that takes a list of numbers and removes all duplicates using a set, then converts it back to a list.
numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers =(set(numbers))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5] (order may vary)
print(list(unique_numbers))  # Output: [1, 2, 3, 4, 5] (order may vary)

# Given a dictionary of products and their prices, find the product with the highest price.
products = {"Laptop": 1000, "Phone": 500, "Tablet": 750}
max_price_product = max(products, key=products.get)
print(max_price_product, products[max_price_product])  # Output: Laptop 1000

min_price_product = min(products, key=products.get)
print(min_price_product)  # Output: Phone

max_value = max(products.values())
print(max_value)  # Output: 1000

# Write a program that merges two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}






