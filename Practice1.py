class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        

    def calc_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is :", sum/3)
    

s1 = Student("Maroof", [98,89,90])
s1.calc_avg()

s1.name = "ironman"
s1.calc_avg()