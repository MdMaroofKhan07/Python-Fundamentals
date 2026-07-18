student = {
    "name" : "Md Maroof Khan",
    "subjects" : {
        "phy" : 89,
        "chem" : 68,
        "math" : 87
    }
}
print(student.keys())
print(list(student.keys())) #typecast
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
pairs = list(student.items())
print(pairs[0])
