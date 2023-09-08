a = ["Ajay", "Sunny", "Rahul", "Rajat", "Kishan", "Rakul", "Tabu"]
user = input ("Enter the Name you want to search\n")
if user in a:
    print ("The name " + str(user) + " is present in the list" )
else:
    print ("The name is not present in list")