# Count the digits in a number

num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count += 1
        num = num // 10

print("Number of digits =", count)

# Count even odd digit
# num = int(input("Enter a number: "))

# count = 0

# while(num>0):
#     digit = num % 10
#     if(digit%2 == 0):
#         count += 1
#     num = num // 10

# print("No. of even digit :",count)