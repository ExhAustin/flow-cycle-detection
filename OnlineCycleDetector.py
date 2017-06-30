
class EdgeData:
	def __init__(self):
		self.count = 0
		self.timestamp = []

class AdjacencyMatrix:
	def __init__(self):
		self.labels = []
		self.graph = []

	def expand(self):
		n0 = len(self.graph)
		n1 = max(n0, 2)
		for i in range(n0):
			self.graph[i] = self.graph[i] + [EdgeData() for t in range(n1)]

		self.graph = self.graph + [[EdgeData() for t in range(n0+n1)] for t in range(n1)]
	
	def addEdge(self, s1, s2, t):
		if not(s1 in self.labels):
			self.labels.append(s1)
		if not(s2 in self.labels):
			self.labels.append(s2)

		x = self.labels.index(s1)
		y = self.labels.index(s2)

		if len(self.graph) < len(self.labels):
			self.expand()

		self.graph[x][y].count += 1
		self.graph[x][y].timestamp.append(t)

	def data(self, i, j):
		return self.graph[i][j].count, self.graph[i][j].timestamp

class OnlineCycleDetector:
	def __init__(self):
