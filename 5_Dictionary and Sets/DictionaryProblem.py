# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one. 
# Use subject name as key and marks as value


marks = {}

x = int(input("Enter phy marks : "))
marks.update({"phy" : x})

x = int(input("Enter chem marks : "))
marks.update({"chem" : x})

x = int(input("Enter math marks : "))
marks.update({"math" : x})

print(marks)

