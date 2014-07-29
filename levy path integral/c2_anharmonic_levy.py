import math, random, pylab

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def V_anharm(x, cubic, quartic):
    return cubic * x ** 3 + quartic * x ** 4    # + x ** 2 / 2

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
        dtau_prime = (N - k) * dtau     #dtau = beta/N
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

#probabilistic weight for a path 'x' using trotter decomposition
def Weight_trott(x):
    return math.exp(sum(-a**2 / 2.0 * dtau for a in x))

#intialization
LevyType = 'free' #choose 'free' or 'harmonic'
beta = 20.0
N = 100
dtau = beta / N
n_steps = 100000
delta = 1.0
x = [0.1] * N
cubic = -1.0
quartic = -cubic
#using the new potential
if(LevyType == 'free'):
    weight_curr = Weight_trott(x) * \
        math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x))
elif(LevyType == 'harmonic'): 
    weight_curr = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x))
data = []
sigma = math.sqrt(1.0 / (2 * math.tanh(beta/2)))
acc = 0.0

#sampling for anharmonic potential with 2 different combinations 
#of Levy Path sampling
for step in range(n_steps):
    N_cut = random.randint(2, N-1)
    x_new = []                          #new path
    new_weight = 0.0
    if(LevyType == 'free'):
        #the addition of x[N_cut] was to improve statistics
        x_new = levy_free_path(x[0], x[N_cut], dtau, N_cut) + x[N_cut:]
        #weight with both harmonic and anharmonic parts
        new_weight = Weight_trott(x_new) * \
            math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x_new))
    elif(LevyType == 'harmonic'):
        x_new = levy_harmonic_path(x[0], x[N_cut], dtau, N_cut) + x[N_cut:]
        #weight with just anharmonic part
        new_weight = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x_new))
    if random.uniform(0.0, 1.0) < new_weight / weight_curr:
        x = x_new[:]
        weight_curr = new_weight
        acc += 1
    x = x[int(N/2):] + x[:int(N/2)]     #wrapping it up
    #if step % 100 == 0:
        #k = random.randint(0, N - 1)
        #for a in x: data.append(a)
    k = random.randint(0, N - 1)
    data.append(x[k])

#print str(acc/n_steps)

pylab.hist(data, bins=50, normed=True, label='QMC')
# this part is irrelevant for this exercise
# x_values = [0.1 * a for a in range (-30, 30)]
# y_values = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
#                   math.exp( - xx **2 * math.tanh( beta / 2.0)) for xx in x_values]
# pylab.plot(x_values, y_values, label='exact')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.xlim(-3.0, 3.0)
pylab.legend()
ProgType = 'levy_' + LevyType + '_path'
pylab.title(ProgType + ' beta = ' + str(beta) + ', dtau = ' + str(dtau) + \
    ', Nsteps = '+ str(n_steps))
pylab.savefig('anharmonic_' + ProgType + str(beta) + '.png')
#pylab.show()