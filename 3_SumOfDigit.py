# Find the sum of digit of a number 
num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits =", sum)


# num = int(input("Enter a number: "))
# product = 1
# while(num>0):
#     digit = num % 10
#     product *= digit
#     num = num // 10

# print("Product of digit :",product)