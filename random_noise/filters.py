import numpy as np
import math

# Gets value of graph while checking limits
def val(x,y,graph,default_val=False, toggle_raise=False):
	if x>=0 and x<graph.shape[0]:
		if y>=0 and y<graph.shape[1]:
			return graph[x][y]
	
	if toggle_raise:
		print('Error: Index exceededed graph boundaries')

	return default_val

# Filters out lone points in the sequence shift graph
def proxFilter(graph):
	proxgraph = np.zeros([graph.shape[0], graph.shape[1]])

	for x in range(graph.shape[0]):
		for y in range(graph.shape[1]):
			result = 0
			if graph[x][y]:
				for x_d in range(-1,2):
					for y_d in range(-1,2):
						if (not(x_d==0 and y_d==0)) and val(x+x_d, y+y_d, graph):
							result = 1
			proxgraph[x][y] = result

	return proxgraph

# Thresholding
def thres(graph, threshold, values=[0,1], equal=True):
	if equal:
		comp = lambda a,b : a>=b
	else:
		comp = lambda a,b : a>b

	graph_out = comp(graph, threshold).astype(int)
	for i in range(graph_out.shape[0]):
		for j in range(graph_out.shape[1]):
			graph_out[i][j] = values[graph_out[i][j]]
	
	return graph_out

# Gradient
def grad(graph, axis=0):
	dim = list(graph.shape)
	dim[axis] -= 1
	graph_out = np.empty(dim)

	for i in range(dim[0]):
		for j in range(dim[1]):
			d_pos = [i, j]
			d_pos[axis] += 1
			graph_out[i][j] = graph[d_pos[0]][d_pos[1]] - graph[i][j]

	return graph_out

# Horizontal Gain Filter
def horizontalGain(x,y,graph,compgraph,params):
	# filter parameters
	h_decay = params[0]
	v_decay = params[1]
	gain = 1 - h_decay*(1 + 2*v_decay)

	# filter
	current = val(x,y,compgraph)
	prev_trans = val(x,y-1,graph,0)
	up_trans = val(x-1,y-1,graph,0)
	down_trans = val(x+1,y-1,graph,0)

	graph[x][y] = gain*current + h_decay*(prev_trans + v_decay*(up_trans + down_trans))
	

# Applies horizontal gain filter to a diagonal slice of sequence shift graph
def hgFilter_slice(head, graph, params=[0.2,0.3]):
	# initialize graphs
	filtergraph = np.zeros([graph.shape[0], graph.shape[1]])

	for x in range(min(head, graph.shape[0]-1), -1, -1):
		y = head - x
		horizontalGain(x,y,filtergraph,graph,params)
		
	return resultgraph

# Applies horizontal gain filter to entire sequence
def hgFilter(graph, params=[0.2,0.3]):
	# filter
	filtergraph = np.zeros([graph.shape[0], graph.shape[1]])

	for x in range(graph.shape[0]):
		for y in range(graph.shape[1]):
			horizontalGain(x, y, filtergraph, graph, params)

	# return result
	return filtergraph

