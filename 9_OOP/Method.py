class Student:

    # Parameterized Constructors
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks  # Instence Level Attribite
        print("adding new student in database....")

    def Greeting(self):
        print("Welcome Students")

    def get_marks(self):
        return self.marks

s1 = Student("Maroof",89)
print(s1.name,s1.marks)
s1.Greeting()
print(s1.get_marks())

s2 = Student("Zaid",99)
print(s2.name,s2.marks)
