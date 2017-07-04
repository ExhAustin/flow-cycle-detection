import sys
from PeriodCounter import OnlinePeriodCounter

if __name__ == '__main__':
	# Create counter
	start = 10
	window = 50
	counter = OnlinePeriodCounter(window, start)

	# Open file
	f = open(sys.argv[1])

	# Feed file lines into counter
	max_nodes = 300
	count = 0

	for line in f:
		node = line.strip('\n')
		counter.addElement(node)

		count += 1
		#if count == max_nodes:
		#	break

	print(counter.count)
