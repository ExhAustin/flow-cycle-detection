import random
from datetime import datetime

def randomNoisySeq(n_char, l_cycle, l_seq, noise):
	alphlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	# generate loop template using params
	random.seed(datetime.now())
	loop_template = []
	for i in range(l_cycle):
		idx = random.randint(0,n_char)
		loop_template.append(alphlist[idx])

	# generate sequence from loop_template with noise
	end_idx = 0
	idx = 0
	seq = []
	while end_idx < l_seq:
		seed = random.randint(0,100)
		if seed > noise*100:
			seq.append(loop_template[idx])
			end_idx += 1
			idx += 1
		else:
			noiseseed = random.randint(0,2)
			if noiseseed == 0:
				idx += 1
			else:
				noisechar = random.choice(alphlist[0:n_char])
				seq.append(noisechar)
				end_idx += 1
				if noiseseed == 1:
					idx += 1

		if idx >= l_cycle:
			idx = 0

	return seq, loop_template
