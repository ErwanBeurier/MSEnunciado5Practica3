


import numpy as np
numbers = [75, 3, 1, 4, 50, 6]
fitVec = []

for i in range(1,100000):
	z = np.random.randint(3,size=(1,5))
	
	total = numbers[0]

	for j in range(0, 5):
		if z[0][j] == 0:
			total += numbers[j]
		elif z[0][j] == 1:
			total *= numbers[j]
		elif z[0][j] == 2:
			total -= numbers[j]

	fitVec.append(abs(852 -total))

print np.shape(fitVec)
#print fitVec
print np.argmin(fitVec)
print 'Best Fitness:\n'
print fitVec[np.argmin(fitVec)]
print '\n'