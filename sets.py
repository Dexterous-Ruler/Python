s={34,23,2,3,22}
print(s)  # Output: {34, 23, 2, 3, 22} (order may vary)
s.add(32)
s.add(322)
print(s)  # Output: {32, 34, 23, 2, 3, 22} (order may vary)
s.remove(2)
print(s)  # Output: {32, 34, 23, 3, 22} (order may vary)
s.discard(36) # No error, 36 is not in the set
print(s)  # Output: {32, 34, 23, 3, 22} (order may vary)


my_set = {1, 2, 3, 4}

my_set.add(5)        # {1, 2, 3, 4, 5}
my_set.remove(2)     # {1, 3, 4, 5}
my_set.discard(10)   # No error if element not found
my_set.pop()         # Removes random element

#set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))   # {1, 2}