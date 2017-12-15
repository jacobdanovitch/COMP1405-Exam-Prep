lst = [[1, 2, 3], ["ha", "ke", "ja"], [3.141, 23.366, 1.010]]

def double(twodim):
	for i in range(len(twodim)):
		for j in range(len(twodim)):
			twodim[i][j] *= 2
	return twodim

print(double(lst))
