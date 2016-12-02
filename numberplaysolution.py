# -*- coding:utf8 -*-

import random



class NumberPlaySolution:
	
	def __init__(self, operations):
		"""
		Constructor. 
		
		Initializes the solution with given operations.
		"""
		self.operations = operations
		
		
	def __eq__(self, other):
		"""
		Checks the equality between this instance and the other instance.
		
		Arguments:
			other		Another instance.
			
		Returns:
			True if the instance has the same string as the other.
			False otherwise.
		"""
		if not isinstance(other, NumberPlaySolution):
			return False
			
		return 	(self.operations == other.operations)
		
		
	def evaluate(self, numbers):
		"""
		Evaluates the solution on the given numbers.
		
		Note:
		I don't check there if numbers has the right number of numbers (that 
		is: len(numbers) = len(self.operations) + 1) because I assume that 
		it's already been checked in the class NumberPlay.
		
		Arguments:
			numbers		A list of numbers to be computed following the rules of
						this instance.
						
		Returns:
			The result of the computations.
		"""
		
		total = 0
		
		for i in xrange(len(numbers)-1):
			if self.operations[i] == '+':
				total += numbers[i]
			elif self.operations[i] == '*':
				total *= numbers[i]
			elif self.operations[i] == '-':
				total -= numbers[i]
		return total
	
	
	def __str__(self):
		"""
		Converts the instance to a string.
		"""
		return "Sol: " + self.operations
	
	
	def mutate(self, index):
		"""
		Randomly changes the value at index "index" of the solution.
		"""
		alphabet = "+-*"
		alphabet = alphabet.replace(self.operations[index], "")
		chosen = random.choice(alphabet)
		self.operations = self.operations[:index] + chosen + self.operations[index+1:]
		
		
	def cut(self, index1, index2 = None, secondHalf = False):
		"""
		Returns a sub-string of this instance.
		
		Arguments:
			index1
			index2		Default: None. If specified, the function will return the substring of the instance beginningfrom 
		"""
		if index2 is None:
			if secondHalf:
				return self.operations[:index1]
			else:
				return self.operations[index1:]
		else:
			return self.operations[index1:index2]
	
	
	
	
	
	