file = open('Files/text1.txt')
text = file.read()
print(text)
if 'computing' in text:
    print("The text is healthy")
else:
    print("The text has a bug")
file.close()