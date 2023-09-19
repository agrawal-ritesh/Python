#creat a Class
class Employee:
    company = "Google"
                  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def empSalary(self): 
        print ("Employee Salary is 50K")

Rohan = Employee()
Rohan.empSalary()