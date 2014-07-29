import math, random, pylab

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def pi_exact(x, beta):
    return math.sqrt(math.tanh(beta/2)) /  math.sqrt(math.pi) * math.exp(-x**2 * math.tanh( beta/2))

beta = 8.0
N = 8
dtau = beta / N
delta = 1.0
n_steps = 100000
x = [0.0] * N     #the array of points along the path
data = []
x_exact = [ 0.01 * a for a in range(-300, 300)]
y_exact = [pi_exact(b, beta) for b in x_exact]

#trotter decomposition is indeed used in the calculation of rho below
'''
This algorithm uses the Trotter decomposition as we can recognize 
the math.exp(-0.5 * dtau * x[k] ** 2) term, which comes from this 
decomposition by the product of two math.exp(-0.5 * dtau * (x[k] ** 2) /2) 
harmonic potential terms that commute as we discussed in B2, question 1.

In rho_free(x_k-1, x_k, beta/N) rho_free(x_k, x_k+1, beta/N), 
there are two factors exp(-beta x^2/4) that combine to exp(-beta x^2/2).
'''
for step in range(n_steps):
    k = random.randint(0, N - 1)
    k_next, k_prev = (k + 1) % N, (k - 1) % N
    x_new = x[k] + random.uniform(-delta, delta)
    #probability of configuration A
    old_weight  = (rho_free(x[k_next], x[k], dtau) * \
                   rho_free(x[k], x[k_prev], dtau) * \
                   math.exp(-0.5 * dtau * x[k] ** 2))
    #probability of configuration B
    new_weight  = (rho_free(x[k_next], x_new, dtau) * \
                   rho_free(x_new, x[k_prev], dtau) * \
                   math.exp(-0.5 * dtau * x_new ** 2))
    #metropolis acceptance rate p(a->b) = min(1, p(b)/p(a))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    #if step%100 == 0:
        #k = random.randint(0, N - 1)
        data.append(x[k])
    #print x

pylab.title('Path Integral Approx. vs Exact')
pylab.hist(data, 100, normed=True, label='Approx.')
pylab.xlabel('$x$')
pylab.ylabel('$\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.plot(x_exact, y_exact,label= 'Exact')
pylab.legend()
pylab.savefig('path_int_harmonic.png')
pylab.show()