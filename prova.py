"""
Just a test class that creates random individuals and 
checks that the best individual fitness is 52

"""


import numpy as np
numbers = [75, 3, 1, 4, 50, 6]
fitVec = []
mat = []

for i in range(1,1000):
	z = np.random.randint(3,size=(1,5))
	mat.append(z)
	total = numbers[0]

	for j in range(0, 5):
		if z[0][j] == 0:
			total += numbers[j]
		elif z[0][j] == 1:
			total *= numbers[j]
		elif z[0][j] == 2:
			total -= numbers[j]

	fitVec.append(abs(852 -total))

order = np.argsort(fitVec)

for i in range(0,20):
	print fitVec[order[i]]
	print mat[order[i]]

print np.argmin(fitVec)
print 'Best Fitness:\n'
print fitVec[np.argmin(fitVec)]
print '\n'