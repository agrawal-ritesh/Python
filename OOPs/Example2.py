'''Let say I created a class and I want to change the it in middle'''

#Create the class.
class Employee:
    #Class Attribute
    company = "Google"

ritesh = Employee()
agrawal = Employee()

print(ritesh.company)
print(agrawal.company)

#Changing the class
Employee.company = "Meta"
print(ritesh.company)
print(agrawal.company)