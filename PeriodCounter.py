import numpy as np
import math
from scipy import stats

class PeriodCounter:
	def __init__(self, window=10, margin=-1):
		self.window = window
		self.margin = margin
		self.reset()

	# Reset
	def reset(self, window=None, margin=None):
		if window is not None:
			self.window = window
		if margin is not None:
			self.margin = margin

		self.seq = []
		self.graph = []
		self.top = 1
		self.left = max(0, self.margin)
		self.elements = 0
		self.count_array = np.zeros(self.window)
		self.count = 0

	# Return count
	def get_count(self):
		return self.count

	# Count an entire sequence
	def countSeq(self, seq):
		for e in seq:
			self.addElement(e)

		return self.count

	# Parse new element
	def addElement(self, e):
		self.elements += 1

		# play dead until end of margin
		if self.elements <= self.left:
			return

		# add element to seq
		if self.margin < 0 or len(self.seq) <= self.window:
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
			if self.margin < 0:
				self.diagShift()
			else:
				self.topShift()

		# mean filtering
		mean = np.mean(self.count_array)
		for i in range(self.window):
			d = self.count_array[i] - mean
			if abs(d) > 1:
				self.count_array[i] -= d

		# mode
		#m = stats.mode(np.round(self.count_array).astype(int))
		#mode = m[0][0]

		# update count
		if self.margin < 0:
			self.count = int(round(2*mean))
			#self.count = 2*mode
		else:
			self.count = int(round(mean))
			#self.count = mode

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

	# Move window right
	def rightShift(self, dist=1):
		for t in range(dist):
			self.graph.pop(-1)
			self.seq.pop(0)

		for row in self.graph:
			row[0:-dist] = row[dist:]
			row[-dist:] = [0]*dist
		self.left += dist

	# Move window diagonally (right-down)
	def diagShift(self):
		self.graph.pop(0)
		self.graph.pop(-1)
		self.seq.pop(0)

		for row in self.graph:
			row[0:-1] = row[1:]
			row[-1] = 0

		self.left += 1
		self.top += 1
