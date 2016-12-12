import numberplaysolution as nps
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

'''
	Mutation variables
'''	
threshold = .5
points = 2

nps = nps.NumberPlaySolution(N)

itCounter = 0

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

	print fit4

	if float(fit4.count(fit4[np.argmin(fit4)]))/len(fit4) >= 0.95:
		break

	itCounter +=1
   
	
#print '\n'
print 'Convergence at iteration number:', itCounter















