#Create a class
class Employee:
    company = "Youtube"

    def empSalary(self, salary): #Parameters
        self.salary = salary #Initialized the Salary Attributes
        print (f"The salary for Employee working at {self.company} is {self.salary}")

ram = Employee()
ram.empSalary(50000)




#Move to Example 6