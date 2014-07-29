import random, math, pylab

#direct sampling of hypershere
def direct_pi_multi(N, D, halflength):
	n_hits = 0
	for n in range(N):
		x = 0
		for d in range(1,D+1):
			x += (random.uniform(-halflength,halflength))**2
			if x > halflength**2:
				break
			elif d == D:
				n_hits += 1
			else:
				continue
	return n_hits

#exact unit hypersphere volume
def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

#initialization values
n_trials = 1000000
dim = 12
L = 1.0

#outputs a table to compare estimated and exact values of unit hypersphere vol
file = open('unit_hypersphere_est_vs_real.txt', 'w')
file.write('----------------------------------------------------------\n')
file.write(str(n_trials) + ' trials\n')
file.write('d | estimation of Vol1_s(d) | Vol1_s(d) (exact) | n_hits\n')
file.write('----------------------------------------------------------\n')
for i in range(1,200):
    num_hits = direct_pi_multi(n_trials, i, L)
    if (num_hits == 0): 
    	break
    vol =  2.0**i* num_hits / float(n_trials)
    file.write('{0:2d}|{1:22.6f}   |{2:16.13f}   | {3}    \n'.format(i, vol, Vol1_s(i),num_hits))
    
#the 22 in the above field for the format class spec is for the extra
#empty spaces in front of the number