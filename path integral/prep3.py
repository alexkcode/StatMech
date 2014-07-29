import pylab, math

def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z
'''
cubic = -0.5
quartic = 0.5

#Potential Well Plot for Quadratic and Quartic Polynomial Potentials
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
y = [V(a) for a in x]
pylab.plot(x, y, label='Quartic')

cubic = 0.0
quartic = 0.0
y = [V(a) for a in x]
pylab.title('Plot of Energy of Polynomial Potentials vs x-position')
pylab.xlabel('x position')
pylab.ylabel('Energy')
pylab.plot(x, y, label='Quadratic')
pylab.legend()
pylab.axis([-4.0, 4.0, 0.0, 3.0])
pylab.savefig('potential_wells.png')

pylab.title('Energy Levels vs Quartic Parameter Value')
pylab.xlabel('x position')
pylab.ylabel('Energy')
for n in range(1,11):
	x = []
	y = []
	for param in range(1000):
		q = float(param)/2000
		c = -q
		x.append(q)
		y.append(Energy(n, c, q))
	pylab.plot(x, y, label=('n = ' + str(n)))
pylab.legend()
#pylab.axis([0.0, 0.5, 0.0, 30.0])
pylab.savefig('energy_vs_quartic.png')

cubic = -0.5
quartic = 0.5
'''
pylab.title('Partition Function Z')
pylab.xlabel('Beta')
pylab.ylabel('Z')
x = [float(i)/10000 for i in range(1,10000)]	#beta
y = [1.0/(2.0*math.asinh(beta/2.0)) for beta in x]
pylab.plot(x, y, label='Exact')
y = [Z(0, 0, i, 20) for i in x]
pylab.plot(x, y, label='Approx.')
pylab.axis([0.0, 1.0, 0.0, 10.0])
pylab.legend()
pylab.savefig('exact_vs_approx_Z.png')
pylab.show()