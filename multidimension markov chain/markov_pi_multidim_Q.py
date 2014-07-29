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
		step = x[d] + random.uniform(-delta,delta)
		z = random.uniform(-delta,delta)
		#replace old dth element with new, updated one with step added in
		test = dist - x[d]**2 + step**2
		if test < limit**2:
			x[d] = step
			n_hits += 1
			dist = test
		if dist + z**2 < limit**2:
			Q_sum += 1
		dist_sum += dist
	#return (n_hits, dist_sum, Q_sum)
	return Q_sum

n_trials = 100000
dim = 200
L = 1.0
vol = [0.0] * 201
vol[1] = Vol1_s(1)

for i in range(2,dim+1):
	vol[i] = 2*float(markov_pi_multidim(n_trials,i,L,L))/n_trials*vol[i-1]

pylab.plot(range(dim+1), vol, 'b')
pylab.gca().set_xscale('linear')
pylab.gca().set_yscale('log')
pylab.xlabel('Dimension')
pylab.ylabel('Volume')
pylab.title('Markov-Chain Calculated Hypersphere Volume')
pylab.savefig('markov_hypersphere_volume.png')
pylab.show()