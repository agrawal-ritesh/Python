'''Static Method'''
'''This method is used when we don't want to use self in class.'''

#Create a class
class Employee:
    company = "Youtube"  #Attribute
#create the Function
    def empSalary(self, salary, signature): #Parameters
        self.salary = salary  #Initialize the Salary Attribute
        self.signature = signature #Initialize the Signature Attribute
        print (f"The salary for Employee working at {self.company} is {self.salary}\n{self.signature}") #output

#use of Static Method. Here we won't use Self.
    @staticmethod
    def text(): #No need to use self.
        print("Hope you get the increment soon!!!") #output

# Creating an instance of Employee
Linda = Employee()
print (Linda.company) #Accessing the class attribute

# Calling the empSalary method with both salary and signature as arguments
Linda.empSalary(100000, "Regards. Linda") 

Linda.text() #Calling static method