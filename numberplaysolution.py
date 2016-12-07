# -*- coding:utf8 -*-

import random
import numpy as np



class NumberPlaySolution:
	
	def __init__(self, N):
		"""
		Constructor. 
		
		Initializes the solution with given operations.   + --> 0, * --> 1, - --> 2
		"""
		self.numbers = [75, 3, 1, 4, 50, 6]
		self.individualMatrix = np.random.randint(3,size=(N,5))
		
		
	def fitness(self, numbers, matrix, numind): 
		"""
		Evaluates the solution on the given numbers.
		
		Note:
		I don't check there if numbers has the right number of numbers (that 
		is: len(numbers) = len(self.operations) + 1) because I assume that 
		it's already been checked in the class NumberPlay.
		
		Arguments:
			numbers		A list of numbers to be computed following the rules of
						this instance.
			numind      len(matrix) total numbers of individuals, children included			
		Returns:
			The result of the computations.
		"""
		
		fitVec = []
		

		for i in range(0, numind):
			
			total = numbers[0]

			for j in range(0, 5):
				if matrix[i][j] == 0:
					total += numbers[j]
				elif matrix[i][j] == 1:
					total *= numbers[j]
				elif matrix[i][j] == 2:
					total -= numbers[j]

			fitVec.append(abs(852 -total)) # Attenzione che quando chiamo questa funzione senza 
										   # valutare tutta la matrice potrebbe essere un problema	

		return fitVec
			
	
	def mutation(self, matrix, numind, N):
		"""
		Randomly changes the value at index "index" of the solution.
		Arguments:
			N 	        Initial population

			numind      Len(matrix) total numbers of individuals, children included

			threshold   Probability of mutation (it can be decreased throughout the iterations)

		"""
		threshold = 0.5   

		for i in range(N,numind):
			if 	np.random.uniform() > threshold:
					matrix[i][random.randint(0,4)] = random.randint(0,2)                 

		return matrix
	
	
	def crossover(self, matrix, fitVec, NM):
	
		"""
		Returns 2*NM mutated individuals
		TODO decidere se fare probabilistic o deterministic crossover, per ora è det.

		"""

		fitVec = np.array(fitVec)
		order = np.argsort(fitVec)  # Vettore ordinato con l'indice dell'elemento col fitness crescente
		                            # Attenzione che gli indici ora partono da zero
		#Ora seleziono e coppie di individui corrispondenti ai primi 6 indici di order
		#Per ora implemento punto di crossover aleatorio
		
		i = 0	
		for j in range(0,NM):                        #cambiando il range cambia il numero di coppie default = 3
			crosspoint = random.randint(1,4)	    #ritorna un intero compreso tra 1 e 4, per scegliere i punti di crossover                               
			tmpvec1 = np.append(matrix[order[i]][:crosspoint],matrix[order[i+1]][crosspoint:]) #first child
			tmpvec2 = np.append(matrix[order[i+1]][:crosspoint],matrix[order[i]][crosspoint:]) #second child
			matrix = np.vstack([matrix,tmpvec1])
			matrix = np.vstack([matrix,tmpvec2])
			i+=2
		
		return matrix


	def replace(self, matrix, fitVec, N):

		"""
		Keeps N best-fitness individuals
		Arguments:
			N 		population initial size

		"""
		#sortvec1 = np.array(fitVec).argsort()[::-1][:len(fitVec)] #vector containing the index in
																 #descending order of fitness values
		sortvec = np.argsort(fitVec)
		tempmatrix = np.empty((0,5), int)
		#print np.shape(tempmatrix.T)
		matrix = np.matrix(matrix)
		#print matrix[sortvec[2]][:].T, np.shape(matrix[sortvec[2]][:].T)
		for i in range(0, N):
			tempmatrix = np.append(tempmatrix, matrix[sortvec[i]][:], axis=0)
			#tempmatrix.append(matrix[sortvec[i]][:])

		
		#print matrix
		#print '\n'
		tempmatrix = np.array(tempmatrix)
		return tempmatrix
















	