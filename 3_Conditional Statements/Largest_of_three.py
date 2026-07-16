a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

if( a>=b and a>=c):
    print("First no. is Largest",a)
elif( b>=c):
    print("Second no. is Largest",b)
else:
    print("Third no. is Largest",c)