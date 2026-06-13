# numbers = [1, 2, 3, 4, 5]
# mixed = [10, "hello", 3.14]
# print(numbers)  # Output: [1, 2, 3, 4, 5]
# print(mixed)    # Output: [10, 'hello', 3.14]
# # Accessing elements        
# print(numbers[0])  # Output: 1
# print(mixed[1])    # Output: 'hello'

# my_list = [1, 2, 3]

# my_list.append(4)   # [1, 2, 3, 4]
# my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
# my_list.remove(2)   # [1, 99, 3, 4]
# my_list.pop()       # Removes last element -> [1, 99, 3]
# my_list.reverse()   # [3, 99, 1]
# my_list.sort()      # [1, 3, 99]
# print(my_list)  # Output: [1, 3, 99]


# squared = [x**2 for x in range(5)]
# print(squared)  # Output: [0, 1, 4, 9, 16]

marks = [85, 92, 78, 90, 88]
extra_marks =[23,44,55]
number=marks.extend(extra_marks)
print(marks)  # Output: [85, 92, 78, 90, 88, 23, 44, 55]

#list comprehension
table = [i * 5 for i in range(1, 11)]
print(table)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
'old method'
a=5
table = []
for i in range(1, 11):
    table.append(a * i)
print(table)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]