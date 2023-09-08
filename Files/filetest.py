f = open ('Files\sample.txt' , 'r') #Specify the correct path. 'r' means, it will read the text present in file.
data = f.read() #opens the file and read it.
print(data) #prints the data present in file.
f.close() #Close the file after reading it.
