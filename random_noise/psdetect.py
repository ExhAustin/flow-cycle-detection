from matplotlib import pyplot as plt
import numpy as np
import scipy.ndimage
import math

from randomSeqGen import randomNoisySeq
import filters

def graphPrint(graph, toggle_bool=True, toggle_slant=True):
	for i in range(graph.shape[0]):
		for j in range(graph.shape[1] - i*toggle_slant):
			if not toggle_bool:
				print(graph[i][j], end='')
			else:
				if graph[i][j]:
					print('O', end='')
				else:
					print('_', end='')
		print()
	print()

if __name__ == '__main__':
	# sequence parameters
	n_char = 8
	l_cycle = 16
	l_seq = 160
	noise = 0.15

	# visualization parameters
	min_eval = 20
	max_repeat = 3
	max_depth = int(max_repeat*l_cycle)
	

	# generate sequence
	seq, loop_ans = randomNoisySeq(n_char, l_cycle, l_seq, noise)

	# display sequence origin
	print('Loop template:')
	print(''.join(loop_ans))
	print('Original sequence:')
	print(''.join(seq))
	print()

	# print shifted sequences graph
	for x in range(max_depth):
		for y in range(l_seq-x):
			s_idx = (y + x) % l_seq
			print(seq[s_idx], end='')
		print()
	print()
		
	# create shifted sequence comparison graph
	if max_depth == 0:
		max_depth = len(seq) - 1

	graph_0 = np.zeros([max_depth+1, len(seq)])
	for x in range(1,max_depth+1):
		for y in range(len(seq)-x):
			graph_0[x][y] = (seq[y + x] == seq[y])

	graphPrint(graph_0, True)
	plt.subplot(3,1,1)
	plt.pcolor(graph_0[::-1])

	"""
	# proximity + horizontal gain filter
	graph_1 = np.copy(graph_0)
	graph_1 = filters.proxFilter(graph_1)
	graph_1 = filters.hgFilter(graph_1, params=[gain, h_decay, v_decay])
	graph_1 = filters.thres(graph_1, threshold)
	graphPrint(graph_1, True)
	"""

	# cw
	graph_2 = np.copy(graph_0)

	#graph_2 = filters.proxFilter(graph_2)
	graph_2 = filters.hgFilter(graph_2, params=[0.4, 0.15])
	graph_2 = scipy.ndimage.filters.gaussian_filter(graph_2, 0.6)
	graph_2 = filters.hgFilter(graph_2, params=[0.4, 0])
	plt.subplot(3,1,2)
	plt.pcolor(graph_2[::-1])

	graph_2 = filters.grad(graph_2)
	plt.subplot(3,1,3)
	plt.pcolor(graph_2[::-1])

	plt.show()

