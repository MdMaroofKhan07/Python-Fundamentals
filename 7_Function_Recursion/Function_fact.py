# WAF to find the factorial of n.( n is the parameter )

def fact_cal(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

fact_cal(5)
