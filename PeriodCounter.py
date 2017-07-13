import numpy as np
import math
from scipy import stats

class PeriodCounter:
	def __init__(self, window=20, start=-1):
		self.counter = OnlinePeriodCounter(start, window)
	
	def count(self, seq):
		for e in seq:
			counter.addElement(e)
		
		return counter.count

class OnlinePeriodCounter:
	def __init__(self, window, start=-1):
		self.window = window
		self.start = start

		self.seq = []
		self.graph = []
		self.top = 1
		self.left = max(0, start)
		self.elements = 0
		self.count_array = np.zeros(self.window)
		self.count = 0

	# Parse two new elements
	def addElement(self, e):
		self.elements += 1

		# play dead until start
		if self.elements <= self.left:
			return

		# add element to seq
		if self.start < 0 or len(self.seq) <= self.window:
			self.seq.append(e)

		# add comparison to each row
		self.graph.append(np.zeros(self.window))
			
		for i in range(len(self.graph)):
			shift = self.top + i
			seq_idx = self.elements - shift - self.left
			self.graph[i][seq_idx] = ( self.seq[seq_idx] == e )

		if len(self.graph) >= self.window:
			# filter completed row
			self.proxFilter(self.graph[0])

			# parse completed row
			for j in range(self.window):
				if self.graph[0][j]:
					self.count_array[j] += 1

			# throw away completed row
			if self.start < 0:
				self.diagShift()
			else:
				self.topShift()

		# denoising
		mean = np.mean(self.count_array)
		for i in range(self.window):
			d = self.count_array[i] - mean
			if abs(d) > 1:
				self.count_array[i] -= (d-1)

		# update count
		if self.start < 0:
			self.count = int(round(2*mean))
		else:
			self.count = int(round(mean))

	# Proimity filter
	def proxFilter(self, arr):
		for i in range(len(arr)):
			if arr[i]:
				left = arr[i-1] if i>0 else False
				right = arr[i+1] if i<len(arr)-1 else False
				if not(left or right):
					arr[i] = False

	# Move window down
	def topShift(self, dist=1):
		for t in range(dist):
			self.graph.pop(0)
		self.top += dist

	# Move window left
	def leftShift(self, dist=1):
		for t in range(dist):
			self.graph.pop(-1)
			self.seq.pop(0)

		for row in self.graph:
			row[0:-dist] = row[dist:]
			row[-dist:] = [0]*dist
		self.left += dist

	# Move window diagonally (left-down)
	def diagShift(self):
		self.graph.pop(0)
		self.graph.pop(-1)
		self.seq.pop(0)

		for row in self.graph:
			row[0:-1] = row[1:]
			row[-1] = 0

		self.left += 1
		self.top += 1
