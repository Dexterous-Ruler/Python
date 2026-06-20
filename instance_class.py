class Employee:
    company="HP"
    def __init__(self, name, salary,bond,company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company
    

    def get_salary(self):
            return self.salary
        
    def get_info(self):
            print(f"The name of the employee is {self.name} and his salary is {self.salary} and his bond is for {self.bond} years")
e1=Employee("Rohit", 34000, 2, "Tesla")

e1.get_info()
print(e1.company)   # will always print instance variable if it is present otherwise it will print class variable
print(Employee.company)  # will always print class variable


# object introspection is the ability to examine the type or properties of an object at runtime. It allows you to inspect the attributes, methods, and other characteristics of an object while the program is running. This can be useful for debugging, understanding the structure of objects, and dynamically interacting with them.
print(dir(e1))  


