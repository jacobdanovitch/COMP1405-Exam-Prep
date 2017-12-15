# Fibonacci sequence

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
	    return f(n-1) + f(n-2) 

print(f(int(input("What n-th value of the Fibonacci sequence do you want to know?"))))
