import math, numpy, pylab

def rho_free(x1, x2, beta):
    return (math.exp(-(x1 - x2) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x1, x2, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x1 ** 2 + x2 ** 2)) \
                         for x1 in grid] for x2 in grid])

def Z_rho_1(rho, dx):
	return numpy.diag(rho).sum() * dx #trace of rho

def Z_rho_2(beta):	#partition func. only for harmonic rho
	return 1/(2 * math.sinh(beta/2))
'''
def normalize_X(X_grid, dx):
	rho = [[rho_free(x1, x2) for x1 in X_grid] for x2 in X_grid]
	rho /= Z_rho_1(rho, dx)
	return rho
'''
#not optimal if we are only concerned about diagonal
def normalize_rho(rho, dx):
	rho /= Z_rho_1(rho, dx)
	return rho

def pi_exact(x, beta):
    return ( math.sqrt(math.tanh(beta/2)) ) / math.sqrt(math.pi) * math.exp(-x**2 * math.tanh(beta/2))

#variable initailization
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-5)
beta     = 2.0 ** (3)
rho = rho_harmonic_trotter(x, beta_tmp)

#exact and trotter approximation comparison
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print('beta = ' + str(beta_tmp) + '	Z_a = ' + str(Z_rho_1(rho, dx)) +\
    	'	Z_b = ' + str(Z_rho_2(beta_tmp)) + '\n')

#trotter vs exact probability comparison plot
y1 = numpy.diag(normalize_rho(rho, dx))
y2 = [pi_exact(x_i, beta) for x_i in x]

pylab.title('Trotter Decomposition vs Exact')
pylab.xlabel('x position')
pylab.ylabel('Probability')
pylab.plot(x, y1, label='$\pi_{trotter}$(x)')
pylab.plot(x, y2, label='$\pi_{exact}$(x)')
pylab.legend()
#pylab.axis([-3.0, 3.0, 0.0, 1.0])
pylab.savefig('trotter_vs_exact.png')
pylab.show()