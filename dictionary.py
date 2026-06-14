student = {"name": "Alice", "age": 21, "grade": "A"}
print(student["name"])  # Output: Alice
student["age"] = 22     # Updating value
student["city"] = "New York"  # Adding new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'A', 'city': 'New York'}

print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # dict_values(['Alice', 22, 'A', 'New York'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ...])

student.pop("age")  # Removes "age" key
print(student)  # Output: {'name': 'Alice', 'grade': 'A', 'city': 'New York'}


student.clear()  # Empties dictionary
print(student)  # Output: {}

#dictionary comprehension
squared = {x: x**2 for x in range(5)}
print(squared)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

dict={}
for i in range(5):
    dict[i]=i**2
print(dict)  # Output: {0: 0, 1: 1,