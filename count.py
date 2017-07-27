import sys
from PeriodCounter import PeriodCounter

if __name__ == '__main__':
	# Create counter
	window = 10
	margin = -1
	counter = PeriodCounter(window, margin)

	# Open file
	f = open(sys.argv[1])

	# Feed file lines into counter
	for line in f:
		node = line.strip('\n')
		counter.addElement(node)

	# Print result
	print(counter.get_count())
