import numberplaysolution as nps
import numpy as np

N = 1000
NM = 300

nps = nps.NumberPlaySolution(N)

'''
fit = nps.fitness(nps.numbers, nps.individualMatrix, N)
#print fit
order = nps.crossover(nps.individualMatrix, fit)
#print order
fit2 = nps.fitness(nps.numbers, order, len(order))
#print fit2
mutatedmat = nps.mutation(order, len(order), N)
#print mutatedmat
fit3 = nps.fitness(nps.numbers, mutatedmat, len(mutatedmat))
#print fit3
repmat = nps.replace(mutatedmat, fit3, N)
print repmat
fit4 = nps.fitness(nps.numbers, repmat, len(repmat))
print fit4
'''
for i in range(0,400):

	fit = nps.fitness(nps.numbers, nps.individualMatrix, N)
	
	order = nps.crossover(nps.individualMatrix, fit, NM)
	fit2 = nps.fitness(nps.numbers, order, len(order))
	mutatedmat = nps.mutation(order, len(order), N)
	fit3 = nps.fitness(nps.numbers, mutatedmat, len(mutatedmat))
	repmat = nps.replace(mutatedmat, fit3, N)	
	fit4 = nps.fitness(nps.numbers, repmat, len(repmat))
	#print fit4
	print fit4[np.argmin(fit4)]   #individuo migliore
	print repmat[np.argmin(fit4)][:]
	nps.individualMatrix = mutatedmat
    