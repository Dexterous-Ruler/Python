'''class person:
    def __init__(self, name,age):
        self.name= name
        self._age= age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if new_age >= 0 and new_age <= 150:
            self._age = new_age
        else:
            print("Invalid age!")
person1 = person("Alice", 20)
print(person1.age)  # Output: 30
person1.age = 35
print(person1.age)  # Output: 35 '''





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age  # Convention: _age for "private" attributes

#     @property  # This makes 'age' a property (the getter)
#     def age(self):
#         return self._age

#     @age.setter # This defines the setter for the 'age' property
#     def age(self, new_age):
#         if new_age >= 0 and new_age <= 150:
#             self._age = new_age
#         else:
#             print("Invalid age!")

# person = Person("Bob", 40)
# print(person.age)    # Output: 40  (Looks like direct attribute access, but calls the getter)
# person.age = 45      # (Calls the setter – looks like attribute assignment)
# print(person.age)
# person.age = -22 #Output: Invalid age!


class MyClass:
    def __init__(self):
        self._internal_value = 0  #  Convention: _ means "private"

    def get_value(self):
        return self._internal_value

obj = MyClass()
# print(obj._internal_value)  # This *works*, but it's against convention
print(obj.get_value())       # This is the preferred way