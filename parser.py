# Parses and filters datasets, then saves to .csv
import sys

def parse(sysargv):
	# arguments from command line
	if len(sysargv) < 3:
		print('Please specify input file and output file name.')
		return
	filename = sysargv[1]
	outfilename = sysargv[2]

	# initialize node list
	node_ls = []

	# parse file
	print('Parsing file: \"{}\"...'.format(filename))
	f = open(filename, 'r')
	for line in f:
		linelist = line.strip().split('\t')
		pos = linelist[1].find('RunBcodeProgame')
		if pos != -1:
			node_str = linelist[1].split('RunBcodeProgame === ')[1]
			node_ls.append(node_str)
		else:
			pos = linelist[1].find('Error')
			if pos != -1:
				node_ls.append(linelist[1])
	f.close()

	# filter out rare occurences?

	# write to file
	print('Writing to file: \"{}\"...'.format(outfilename))
	f = open(outfilename, 'w')
	for node_str in node_ls:
		f.write(node_str)
		f.write('\n')
	f.close()	

if __name__== '__main__':
	parse(sys.argv)
