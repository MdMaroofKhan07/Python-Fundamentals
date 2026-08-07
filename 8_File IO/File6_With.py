with open("Sample.txt","r") as f:
    data = f.read()
    print(data)

with open("Sample.txt","w") as f:
    f.write("new data")