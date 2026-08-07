# f = open("Sample.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# f = open("Sample.txt","w+")
# print(f.read())
# f.write("Hey What are you doing")
# f.close()

f = open("Sample.txt","a+")
print(f.read())
f.write("Hey What are you doing")
f.close()
