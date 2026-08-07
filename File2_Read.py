f = open("demo.txt","r")

line1 = f.readline() # read one line at a time
print(line1)
line2 = f.readline()
print(line2)
f.close()