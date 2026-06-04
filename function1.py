square = lambda x: x * x
print(square(4))  # Output: 16

'''def square(x):
    return x * x
    print(square(4))  # Output: 16'''
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

'''def number(x):
    return x**2
numbers = [1, 2, 3, 4]
squared = list(map(number, numbers))
print(squared)  # Output: [1, 4, 9, 16] '''