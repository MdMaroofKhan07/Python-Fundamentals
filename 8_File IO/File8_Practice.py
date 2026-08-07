# f = open("practice.txt","w")

# f.write("Hi everyone \nwe are learning File IO\nusing Java\nI Like programming in Java.")

# f.close()

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File IO\n")
#     f.write("using Java.\nI like programming in Java")

# change java to python everywhere

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# Write a function to Search if learning is present or not
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")

check_for_word()
