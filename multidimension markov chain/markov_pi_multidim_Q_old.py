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
	for n in range(N):
		d = random.randint(0, D-1)
		step = random.uniform(-delta,delta)
		z = random.uniform(-delta,delta)
		#replace old dth element with new, updated one with step added in
		change = -x[d] + step**2
		test = dist + change
		if test < limit**2:
			x[d] += change
			n_hits += 1
			dist = test
		if dist + z**2 < limit**2:
			Q_sum += 1
		dist_sum += dist
	#return (n_hits, dist_sum, Q_sum)
	return Q_sum

n_trials = 100000
dim = 199
L = 1.0

result = markov_pi_multidim(n_trials, dim, L, L)

print '2 * <Q> = ', 2*float(result[2])/n_trials
print 'Vol1_s(',dim + 1,') / Vol1_s(',dim,') = ' , float(Vol1_s(dim + 1)) / Vol1_s(dim)