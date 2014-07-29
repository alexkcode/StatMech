import random, math, pylab

#direct sampling of hypshere
def direct_pi_multi(D,N, halflength):
	n_hits = 0
	for n in range(N):
		x = 0
		for d in range(1,D+1):
			#print('I ran for ' + str(d) + ' x ' + str(n) + ' iterations and I better not stop!')
			x += (random.uniform(-halflength,halflength))**2
			#print('d = ' + str(d) + ' ' + 'x = ' + str(x))
			#print('d = ' + str(d) + '	' + str(n_hits) + '	x = ' + str(x))
			if x > halflength**2:
				#print('BREAK! BREAK! BREAK! BREAK! BREAK! BREAK! BREAK! BREAK!')
				break
			elif d == D:	#needed the offset since the count starts at 0!!!
				#print('end of loop\n')
				#print('HIT! HIT! HIT! HIT! HIT! HIT! HIT! HIT! HIT! HIT! HIT! ')
				n_hits += 1
				#print('we have ' + str(n_hits) + ' hits')
			else:
				continue
		#print(str(n_hits))
	return n_hits

#exact unit hypersphere volume
def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

#initialization values
n_trials = 1000000
dim = 12
L = 1.0

'''
test = direct_pi_multi(dim, n_trials, L)
print(str(float(test)/n_trials))
'''
#'''
#outputs a table to compare estimated and exact values of unit hypersphere vol
file = open('unit_hypersphere_est_vs_real.txt', 'w')
file.write('--------------------------------------------------------\n')
file.write('n_trials used for all\n')
file.write('d | estimation of Vol1_s(d) | Vol1_s(d) (exact) | n_hits\n')
file.write('--------------------------------------------------------\n')
for i in range(1,dim+1):
	hits = direct_pi_multi(int(i), n_trials, L)
	file.write(str(i).zfill(2) + '  ' + str(4.0*float(hits)/n_trials).zfill(8) \
		+ '                  ' + str(Vol1_s(i)).zfill(13) \
		+ '       ' + str(hits).zfill(7) + '\n')
file.close()
#'''