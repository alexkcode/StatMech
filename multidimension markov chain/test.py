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
		step = random.uniform(-delta,delta)
		z = random.uniform(-delta,delta)
		#replace old dth element with new, updated one with step added in
		change = -x[d] + step**2
		test = dist + change
		if test < limit**2:
			x[d] += change
			#n_hits += 1
			dist = test
		if dist + z**2 < limit**2:
			Q_sum += 1
		dist_sum += dist
	#return (n_hits, dist_sum, Q_sum)
	return Q_sum

error_table = open('error_table.txt', 'w')

dim = 20

error_table.write('n_trials | <Vol1_s(20)> |  Error  | Vol1_s(20) (exact result) |')
markov_vol = [0.0] * 6
markov_vol_sq = markov_vol
for i in range(6):
	vol = Vol1_s(1)
	for j in range(2,dim+1):
		Q_avg = float(markov_pi_multidim(10**i, j, L, L))
		vol *= 2*Q_avg/n_trials
	markov_vol[i] = vol
	markov_vol_sq[i] = vol**2
	size = len(markov_vol)
	mean_m_vol = sum(markov_vol)/size
	mean_m_vol_sq = sum(markov_vol_sq)/size
	#the numerator below is the variance of the computate hypshere volume
	error = math.sqrt(abs(mean_m_vol_sq - mean_m_vol**2))/math.sqrt(20)
	error_table.write('{1:6} | {2:12.10} | {3:7.5} | {4:16.14} '.format(10**i, \
		markov_vol, error, Vol1_s(dim))