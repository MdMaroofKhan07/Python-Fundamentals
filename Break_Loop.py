# i = 1
# while i <= 5 :
#     print(i)
#     if( i == 3 ) :
#         break
#     i += 1

# print("End of loop")

#Break
tup = ( 1,4,9,16,25,36,49,64,81,100,36 )

x = int(input("Enter number :"))

i = 0

while i < len(tup) :
    if(tup[i] == x):
        print("Found at index", i)
        break
    else:
        print("Finding.....")
    i += 1