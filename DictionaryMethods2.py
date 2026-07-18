student = {
    "name" : "Md Maroof Khan",
    "subjects" : {
        "phy" : 89,
        "chem" : 68,
        "math" : 87
    }
}
# print(student["name2"]) #error
print(student.get("name2")) #no error = None

student.update({"city" : "Ghazipur"})
print(student)