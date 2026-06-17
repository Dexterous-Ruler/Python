# Create a class Car with a method drive() that prints "Car is moving".
# Create an object of Car and call drive().
class Car:
    def drive(self):
        print("Car is moving.")

car = Car()
car.drive()

# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1= person("Alice",30)
print(f"Name: {person1.name}, Age: {person1.age}")


# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

class animal:
    def sound(self):
        print("Some sound")
class dog(animal):
    def sound(self):
        print("Bark!")  
dog1= dog()
dog1.sound()



    