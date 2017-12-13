def double(twodim):
    for i in range(len(twodim)):
        for j in range(len(twodim[i])):
            twodim[i][j] *= 2
    return twodim


test = [
        [1, "hello"],
        ["world", 4],
        [12, 3],
        ["x", "y"]
    ]

for row in test:
    print(row)

print()

doubletest = double(test)

for row in doubletest:
    print(row)