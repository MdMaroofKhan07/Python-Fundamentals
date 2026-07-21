# Print the elements of the following list using for loop:
# [1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val)

# Search for a number x in this tuple using loop :
# (1,4,9,16,25,36,49,64,81,100)

tup = ( 1,4,9,16,25,36,49,64,81,100,49 )

x = int(input("Enter number :"))

idx = 0
for el in tup:
    if(el == x):
        print("Number found at index", idx)
    idx += 1

