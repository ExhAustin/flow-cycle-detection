from matplotlib import pyplot as plt
import numpy as np
import sys
import scipy.ndimage
import math

if __name__ == '__main__':
	# visualization parameters
	max_depth = 300

	# parse sequence
	seq = []
	f = open(sys.argv[1])
	for line in f:
		seq.append(line.strip('\n'))
		
	# create shifted sequence comparison graph
	if max_depth == 0:
		max_depth = len(seq) - 1

	graph_0 = np.zeros([max_depth+1, max_depth+1])
	for x in range(1,max_depth+1):
		for y in range(max_depth+1-x):
			graph_0[x][y] = (seq[y + x] == seq[y])


	plt.pcolor(graph_0[::-1])
	plt.show()
