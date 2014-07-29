import math, random, pylab

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
        #x = x[int(N/2):] + x[:int(N/2)]  #wrapping
    return x

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

def Weight_trott(x):
    return math.exp(sum(-a **2/ 2.0 * dtau for a in x))

beta = 20.0
N = 80
dtau = beta / N
n_steps = 100000
delta = 5
x = [2.0] * N
weight_curr = Weight_trott(x)
data = []
sigma = math.sqrt(1.0 / (2 * math.tanh(beta/2)))
acc = 0.0
for step in range(n_steps):
    N_cut = random.randint(1, N-2)
    new_path = levy_free_path(x[0], x[N_cut], dtau, N_cut) + x[N_cut:]
    new_weight = Weight_trott(new_path)
    if random.uniform(0.0, 1.0) < new_weight / weight_curr:
        x = new_path[:]
        weight_curr = new_weight
        acc += 1
    if step % 100 == 0:
        #k = random.randint(0, N - 1)
        for a in x: data.append(a)
    x = x[int(N/2):] + x[:int(N/2)]     #wrapping it up

print str(acc/n_steps)

pylab.hist(data, bins=50, normed=True, label='QMC')
x_values = [0.1 * a for a in range (-30, 30)]
y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
                  math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.axis([-3.0, 3.0, 0.0, 0.6])
pylab.legend()
ProgType = 'levy_free_path'
pylab.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + ', Nsteps = '+ str(n_steps))
pylab.savefig(ProgType + str(beta) + '.png')
pylab.show()