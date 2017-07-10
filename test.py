import sys
from PeriodCounter import OnlinePeriodCounter

if __name__ == '__main__':
	# Load file
	f = open(sys.argv[1])

	# Count cycles by occurence of a single node
	count = 0
	for line in f:
		node = line.strip('\n')
		if node == 'P10':
			count += 1

	# Print result
	print(count)
