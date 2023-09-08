employee = int(input("Enter your age"))
if (employee>21 and employee<55):
    print("You are eligible to participate")
elif(employee>=18 and employee<21):
    print("Take the permission from manager and participate")
else:
    print("You are no elegible to participate")