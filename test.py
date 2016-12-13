import numberplaysolution
import numpy as np

"""
Parameters
	N          Population size

	NM 		   Number of pairs to be crossed,
		       giving birth to 2*NM children

	iter       number of iterations

	threshold  1-probability of mutation 
			   (the lower the number, the higher
			    the probability of mutation)

	points     Number of times the offspring can mutate
	    
	TODO       mutation probability decreasing in times
"""

N = 20
NM = 5
iterations = 1000
nSimul = 100

'''
	Mutation variables
'''	
threshold = .5
points = 1
bestFitVec = []
meanVec = 0.


for v in range(0,nSimul):

	itCounter = 0
	nps = numberplaysolution.NumberPlaySolution(N)

	for i in range(0,iterations):


		fit = nps.fitness(nps.numbers, nps.individualMatrix, N)
		crossMat = nps.probCrossover(nps.individualMatrix, fit, NM)

		fit2 = nps.fitness(nps.numbers, crossMat, len(crossMat))
		mutatedMat = nps.mutation(crossMat, len(crossMat), N, threshold, points)

		fit3 = nps.fitness(nps.numbers, mutatedMat, len(mutatedMat))
		repMat = nps.replace(mutatedMat, fit3, N)

		fit4 = nps.fitness(nps.numbers, repMat, len(repMat))
		#print fit4[np.argmin(fit4)]             #Best individual fitness
		#print repMat[np.argmin(fit4)][:]        #Best individual
		nps.individualMatrix = repMat

		#print fit4

		itCounter +=1

		if float(fit4.count(fit4[np.argmin(fit4)]))/len(fit4) >= 0.95:
			break

	bestFitVec.append(fit4[np.argmin(fit4)])		
	meanVec += itCounter
	#print itCounter

print 'Average number of iterations'
print '\n'
print meanVec/nSimul
print '\n'
print 'BestFitVEc'
print bestFitVec
#print '\n'
#print 'Convergence at iteration number:', itCounter















