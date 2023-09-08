def college(avg):
    average = (sum(avg) / len(avg))
    return average

avg1 = []
number = int (input("How many Subjects are there "))
for i in range(number):
    marks = int (input("Enter the Marks obtained"))
    avg1.append(marks)

avg2 = []
number2 = int (input("How many Subjects are there "))
for j in range(number2):
    marks2 = int (input("Enter the Marks obtained"))
    avg2.append(marks2)
average1 = college(avg1)
average2 = college(avg2)

print("The avg marks obtained is ", average1 , average2)
