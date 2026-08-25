# Last Digit

# num = int(input("Enter a number: "))

# last_digit = num % 10

# print("Last digit =", last_digit)


# First Digit

num = int(input("Enter a number: "))

while( num >= 10 ):
    num = num // 10

print("First digit = ", num)