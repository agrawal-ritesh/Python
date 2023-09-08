# Que
'''Print the value to tell if the student if passed of failed in exam
less than 33% is failed. Student need atleast 33% to pass.
Take the value from teacher'''

#----------------------------------------------------------------------------------

sub1 = int(input("Enter the number\n"))
sub2 = int(input("Enter the number\n"))
sub3 = int(input("Enter the number\n"))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are failed")
elif ((sub1+sub2+sub3) / 3) <40:
    print("You are less than 40")
else:
    print ("YTou are passed")

