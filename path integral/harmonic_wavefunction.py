import math, pylab, numpy

n_states = 40
Energies = [0.5 + i for i in range(n_states)]
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
#the following loop sets up the wavefunction vector psi
for x in grid_x:
 	psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
	psi[x].append(math.sqrt(2.0) * x * psi[x][0])
	for n in range(2, n_states):
		psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] - \
			math.sqrt((n - 1.0) / n) * psi[x][n - 2])

def Z_1(E, beta):
	return sum([math.exp(-beta * energy) for energy in E])

def Z_2(N, X, E, psi, beta, dx):
	rho = [[sum([math.exp(-beta * E[i]) * psi[x1][i] * psi[x2][i] \
		for i in range(N)]) for x1 in grid_x] for x2 in grid_x]
	rho_sum = numpy.diag(rho).sum() * dx
	rho /= rho_sum	
	return (rho,rho_sum)

#this function gives an incorrect rho_sum (or something else is wrong)
def Z_2_old(N, X, E, psi, beta, dx):
	rho_sum = 0
	for x in grid_x:
		rho_sum += sum([math.exp(-beta * E[i]) * psi[x][i]**2 for i in range(N)]) * dx
	return rho_sum

def Z_3(beta):
	return 1/(2*math.sinh(beta/2))
'''
print(str(Z_1(Energies, 2)) + '\n')
print(str(Z_2(n_states, grid_x, Energies, psi, 2, 0.2)) + '\n')
print(str(Z_3(2.0)))
'''
beta = 2.0
dx = 0.2

rho = Z_2(n_states, grid_x, Energies, psi, 2, 0.2)[0]
rho_diag = numpy.diag(rho)
#why isn't following formula right?
'''
pi = [sum([math.exp(-beta * Energies[i]) * psi[x][i]**2 for i in range(n_states)]) * dx\
	/Z_2_old(n_states, grid_x, Energies, psi, 2, 0.2) for x in grid_x]
'''

pylab.title('Plot of Probabilty of Particle in Harmonic Well')
pylab.xlabel('x position')
pylab.ylabel('Probability')
pylab.plot(grid_x, rho_diag, label='$\pi$(x)')
pylab.legend()
pylab.axis([-3.0, 3.0, 0.0, 1.0])
pylab.show()
