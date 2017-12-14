def cumulativesum(n):
    if n == 1:
        return n
    else:
        return n + cumulativesum(n-1)

print(cumulativesum(50))