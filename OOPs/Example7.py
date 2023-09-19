'''OOPs Constructor'''
'''__init__''' #Also know as Constructor
'''It automatically runs when executed.'''

#Create a class
class Employee:
    company = "Youtube"

    def __init__(self):
        print("I am the Constructor")

    def empSalary(self, salary): #Parameters
        self.salary = salary #Initialized the Salary Attributes
        print (f"The salary for Employee working at {self.company} is {self.salary}")

ram = Employee()

#When the instance is assigned to the class, the __init__ method will autmatically run and gives the Output.

