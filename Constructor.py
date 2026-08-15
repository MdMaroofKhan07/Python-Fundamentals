class Student:

    collage = "AMU" # Class level attribute

    # Default Constructors
    def __init__(self):
        pass

    # Parameterized Constructors
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks  # Instence Level Attribite
        print("adding new student in database....")

s1 = Student("Maroof",89)
print(s1.name,s1.marks)

s2 = Student("Zaid",99)
print(s2.name,s2.marks)
print(s2.collage)