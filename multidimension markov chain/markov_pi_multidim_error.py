import math, random, pylab

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

def dot(x,y):	#takes in list args.
	return sum([a*b for a in x for b in y if a==b])

#W.I.P.
def markov_pi_multidim(N, D, delta, limit):
	x = [0.0] * D
	n_hits = 0
	dist_sum = 0
	Q_sum = 0
	dist = 0	#dot(x,x)
	#vol = [0.0] * D
	for n in range(N):
		d = random.randint(0, D-1)
		step = x[d] + random.uniform(-delta,delta)
		z = random.uniform(-delta,delta)
		#replace old dth element with new, updated one with step added in
		test = dist - x[d]**2 + step**2
		if test < limit**2:
			x[d] = step
			dist = test
		if dist + z**2 < limit**2:
			Q_sum += 1
	return Q_sum

error_table = open('error_table.txt', 'w')

dim = 20
L = 1.0

#not giving the right numbers... the values are too low for the highest number of trials
error_table.write('n_trials | <Vol1_s(20)> |     Error    |'\
	' Vol1_s(20) (exact result) |\n')
markov_vol = [0.0] * 6
markov_vol_sq = markov_vol
for i in range(6):
	n_trials = 10**i
	vol = 2.0
	for j in range(2,dim+1):
		Q = float(markov_pi_multidim(n_trials, j, L, L))
		vol *= 2.0*Q/n_trials
	markov_vol.append(vol)
	markov_vol_sq.append(vol**2)
	size = len(markov_vol)
	mean_m_vol = sum(markov_vol)/size
	mean_m_vol_sq = sum(markov_vol_sq)/size
	#the numerator below is the variance of the computed hypershere volume
	error = math.sqrt(abs(mean_m_vol_sq - mean_m_vol**2))/math.sqrt(float(size))
	error_table.write(' {0:7} | {1:11} | {2:11.9} | {3:16.14} \n'.\
		format(n_trials, vol, error, Vol1_s(dim)))