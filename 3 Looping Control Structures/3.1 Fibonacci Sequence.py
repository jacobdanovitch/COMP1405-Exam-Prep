def fibonacci():
    val1 = 0
    val2 = 1
    n = int(input("What n-th value of the Fibonacci sequence do you want to know?"))
    for i in range(n-1):
        temp = val1
        val1 += val2
        val2 = temp
        print(val1, val2)
    return val1

print(fibonacci())