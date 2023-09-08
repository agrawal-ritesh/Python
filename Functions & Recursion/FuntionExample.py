def percentage (marks):
    p = ((sum(marks)/4)*100)
    return p 

marks1 = [24,77,45,32]
percentage1 = percentage(marks1)

marks2 = [44,65,22,90]
percentage2 = percentage(marks2)

print (percentage1, percentage2)