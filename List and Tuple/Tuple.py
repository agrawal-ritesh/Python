#Tuple values can't be changed. It it similar to list only but we can chane its value. 

tup = [33,21,345,221,464]
print(tup)
print(tup[3])

#-----------------------------------------
tup.insert(3112)   #it will throw the error. 
print(tup)

#----------------------------------------
tup[2] = 54 #this will throw error.
print(tup)