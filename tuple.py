my_tuple = (10, 20, 30)
single_element = (5,)  # Tuple with one element (comma required)
print(my_tuple)  # Output: (10, 20, 30)
print(single_element)  # Output: (5,)

print(my_tuple[1])  # Output: 20

#tuple unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: 10 20 30

# methods

my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2))  # Output: 2

print(my_tuple.index(3))   # Output: 3
print(my_tuple.index(2))   # Output: 1 (first occurrence of 2)