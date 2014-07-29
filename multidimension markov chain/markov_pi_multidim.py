import math, random, pylab

def dot(x,y):	#takes in a list arg.
	return sum([a*b for a in x for b in y if a==b])

def markov_pi_multidim(N, D, delta, limit):
	x = [0.0 for i in range(D)]
	n_hits = 0
	dist_sum = 0
	for n in range(N):
		d = random.randint(0,D-1)
		test = [a for a in x]
		test[d] += random.uniform(-delta, delta)
		dist = dot(test,test)
		if dist < limit**2:
			x = test
			n_hits += 1
		dist_sum += dot(x,x) 	#since the average involves non-hits as well
	return (n_hits, dist_sum)
'''
test = markov_pi_multidim(100000,2,1,1)
print(str(test[0]) + ' ' + str(float(test[1])/100000))
'''