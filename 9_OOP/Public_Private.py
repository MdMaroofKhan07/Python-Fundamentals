# class Account:
#     def __init__(self, acc_no , acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # We are keeping it private by using __

# acc1 = Account("1234" , "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)

class Person:
    __name = "Maroof"  # Making variable private

    def __hello():
        print("Hello World")

p1 = Person()
print(p1.__name)
print(p1.__hello())