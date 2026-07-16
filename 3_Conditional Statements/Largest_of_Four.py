a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
d = int(input("Enter fourth number :"))

if( a>=b and a>=c and a>d):
    print("First no. is Largest",a)
elif( b>=c and b>=d):
    print("Second no. is Largest",b)
elif( c>=d):
    print("Third no. is Largest",c)
else:
    print("Fourth no. is Largest",d)