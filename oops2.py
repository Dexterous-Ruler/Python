class Employee:
    def __init__(self, name, salary,bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    

    def get_salary(self):
            return self.salary
        
    def get_info(self):
            print(f"The name of the employee is {self.name} and his salary is {self.salary} and his bond is for {self.bond} years")
e1=Employee("Rohit", 34000, 2)

e1.get_info()