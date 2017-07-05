import sys
from PeriodCounter import OnlinePeriodCounter

if __name__ == '__main__':
	# Create counter
	start = -1
	window = 50
	counter = OnlinePeriodCounter(window, start)

	# Open file
	f = open(sys.argv[1])

	# Feed file lines into counter
	for line in f:
		node = line.strip('\n')
		counter.addElement(node)

	# Print result
	print(counter.count)
