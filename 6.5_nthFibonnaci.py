n = int(input("Enter the value of n: "))

a = 0
b = 1

if n == 1:
    print("1st Fibonacci number =", a)
elif n == 2:
    print("2nd Fibonacci number =", b)
else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print(f"{n}th Fibonacci number =", b)