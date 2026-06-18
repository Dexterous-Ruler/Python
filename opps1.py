"a class is defined as the barebone structure which can be used to create objects"
# Four Pillars of OOPs
# 1. Encapsulation :' Encapsulation bundles data (attributes) and the methods that operate on that data within a class. This protects the data from being accidentally changed or misused from outside the object. It controls access.
# 2. Inheritance :' Inheritance allows a class to inherit attributes and methods from another class. This promotes code reusability and establishes a hierarchical relationship between classes.
# 3. Polymorphism :' Polymorphism allows objects of different types to be treated as instances of the same type through a common interface.
# 4. Abstraction :'' Abstraction means hiding complex details and showing only the essential information to the user.

" object is the specific instance created from a class. It is a real-world entity that has attributes and behaviors defined by the class. An object is created using the class as a blueprint, and it can have its own unique values for the attributes defined in the class."
"class is a blueprint or a template for creating objects. It defines the attributes (data) and methods (functions) that the objects created from the class will have. A class is a user-defined data type that encapsulates data and functions into a single unit. It serves as a blueprint for creating multiple objects with similar characteristics and behaviors."

class Employee:
    company="HP"

    def get_salary(self): #self is important here because self is a way to refer to the instance of the class that is calling the method. It allows you to access the attributes and methods of that specific instance. When you call a method on an object, Python automatically passes the object itself as the first argument to the method, which is conventionally named self.
        print(self)
        return 34000
    

e=Employee() # creating an object of the class Employee
print(e.get_salary())

e2=Employee()
print(e2.get_salary())
print(e2.company)
   
