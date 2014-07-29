import math, random, pylab, numpy

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        #used for calculation of sigma and mean
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        #random.gauss(mean, sigma)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
        #wrapping, this "moves" x to the middle
        #x = x[int(N/2):] + x[:int(N/2)]
    return x

beta = 10.0
N = 80
dtau = beta / N
n_steps = 100000
delta = 5
x = [2.0] * N
data = []
sigma = math.sqrt(1.0 / (2 * math.tanh(beta/2)))
for step in range(n_steps):
    x_start = random.gauss(0.0, sigma)
    path = levy_harmonic_path(x_start, x_start, dtau, N)
    if step % 1 == 0:
        k = random.randint(0, N - 1)
        data.append(path[k])

pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                  math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.legend()
ProgType = 'levy_harm_path'
pylab.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()