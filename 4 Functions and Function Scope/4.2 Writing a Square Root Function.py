def root(x):
    return x**(1/2)

print(root(9), root(16))

#https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python
def newton(n):
    approx = n / 2.0
    while True:
        better = (approx + n / approx) / 2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better

print(newton(9), newton(16))