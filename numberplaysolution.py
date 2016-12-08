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
		#print self.individualMatrix
		#print 'initMat\n'
		
	def fitness(self, numbers, matrix, numind): 
		"""
		Evaluates the solution on the given numbers.
		
		Note:
		I don't check there if numbers has the right number of numbers (that 
		is: len(numbers) = len(self.operations) + 1) because I assume that 
		it's already been checked in the class NumberPlay.
		The following coding scheme has been adopted:

		+ --> 0, 
		* --> 1, 
		- --> 2.

		Arguments:
			numbers		A list of numbers to be computed following the rules of
						this instance.
			matrix      The matrix of the individual we want to evaluate the fitness of
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
			
	
	def mutation(self, matrix, numind, N, threshold, points):
		"""
		Randomly changes a digit of the children.

		Arguments:
			N 	        Initial population

			numind      Len(matrix) total numbers of individuals, children included

			threshold   1-Probability of mutation (it can be decreased throughout the iterations)

			points      Number of elements of the individual to be mutated 1 <= points <= 5

		"""   
		for p in range(0,points):
			for i in range(N,numind):
				if 	np.random.uniform() > threshold:
						matrix[i][random.randint(0,4)] = random.randint(0,2)                 

		return matrix
	
	
	def crossover(self, matrix, fitVec, NM):
	
		"""
		Returns 2*NM mutated individuals
		TODO decidere se fare probabilistic o deterministic crossover, per ora è det.
		
		Arguments:

			matrix  Matrix of individuals

			fitVec  Vector with fitness values of the
					individuals in the matrix
			NM      Number of pairs to be crossed,
		            giving birth to 2*NM children
		"""
		
		#fitVec = np.array(fitVec, 'double')
		fitVec = np.array(fitVec)

		order = np.argsort(fitVec)  # Vettore ordinato con l'indice dell'elemento col fitness crescente
		                            # Attenzione che gli indici ora partono da zero
		#Ora seleziono e coppie di individui corrispondenti ai primi 6 indici di order
		#Per ora implemento punto di crossover aleatorio
		
		i = 0	
		for j in range(0,NM):                        
			crosspoint = random.randint(1,4)	    #ritorna un intero compreso tra 1 e 4, per scegliere i punti di crossover                               
			tmpvec1 = np.append(matrix[order[i]][:crosspoint],matrix[order[i+1]][crosspoint:]) #first child
			tmpvec2 = np.append(matrix[order[i+1]][:crosspoint],matrix[order[i]][crosspoint:]) #second child
			matrix = np.vstack([matrix,tmpvec1])
			matrix = np.vstack([matrix,tmpvec2])
			i+=2
		
		return matrix


	def probCrossover(self, matrix, fitVec, NM):
	
		"""
		Same as previuos crossover function, but now the selection
		of the parents is probabilistic
		
		Arguments:

			matrix  Matrix of individuals

			fitVec  Vector with fitness values of the
					individuals in the matrix
			NM      Number of pairs to be crossed,
		            giving birth to 2*NM children
		"""
		
		fitVec = np.array(fitVec, 'double')
		probVec = fitVec
		order = []

		for i in range(0,len(fitVec)):
			probVec[i] = (1/fitVec[i]) 
			

		probVec = probVec/(sum(probVec))
	

		for k in range(0,2*NM):
			randVec = []
			for h in range(0,len(fitVec)):
				randVec.append(np.random.uniform())
		 	order.append(np.argmax(randVec*probVec))

		
		i = 0	
		for j in range(0,NM):                        
			crosspoint = random.randint(1,4)	    #ritorna un intero compreso tra 1 e 4, per scegliere i punti di crossover                               
			tmpvec1 = np.append(matrix[order[i]][:crosspoint],matrix[order[i+1]][crosspoint:]) #first child
			tmpvec2 = np.append(matrix[order[i+1]][:crosspoint],matrix[order[i]][crosspoint:]) #second child
			matrix = np.vstack([matrix,tmpvec1])
			matrix = np.vstack([matrix,tmpvec2])
			i+=2
		
		return matrix

	def replace(self, matrix, fitVec, N):

		"""
		Keeps N best-fitness individuals, sorts the new matrix
		by ascending fitness values

		Arguments:
			N 		population initial size

		"""
		
		sortvec = np.argsort(fitVec)
		tempmatrix = np.empty((0,5), int)
		matrix = np.matrix(matrix)
		
		for i in range(0, N):
			tempmatrix = np.append(tempmatrix, matrix[sortvec[i]][:], axis=0)

		tempmatrix = np.array(tempmatrix)

		return tempmatrix


	def probReplace(self, matrix, fitVec, N):

		"""
		Same as before but the replacement is now 
		probabilistic

		Arguments:
			N 		population initial size

		"""
		
		fitVec = np.array(fitVec, 'double')
		probVec = fitVec
		order = []

		for i in range(0,len(fitVec)):
			probVec[i] = fitVec[i]/sum(fitVec)
		

		for k in range(0,N):
			randVec = []
			for h in range(0,len(fitVec)):
				randVec.append(np.random.uniform())
		 	order.append(np.argmax(randVec*probVec))

		print order

		tempmatrix = np.empty((0,5), int)
		matrix = np.matrix(matrix)
		
		for i in range(0, N):
			tempmatrix = np.append(tempmatrix, matrix[sortvec[i]][:], axis=0)

		tempmatrix = np.array(tempmatrix)

		return tempmatrix













	