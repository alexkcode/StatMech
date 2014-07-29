import random, math, pylab, os.path

# Levy Construction for a path under a 3D harmonic potential
# k corresponds to the length of a cycle in the path
def levy_harmonic_path(k, beta):
    # choosing our beginning point with a Gaussian distribution
    x_k = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 * \
        math.tanh(k * beta / 2.0))) for d in range(3)])
    # initializing our path 
    x = [x_k]
    for j in range(1, k): 
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
            math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + x_k[d] / \
            math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        # here's where the action takes place!
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x

# Analytic solution for 3D harmonic potential well probability density
def rho_harm(x, xp, beta):
    # here upsilon_1 and upsilon_2 are just exponents
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 * \
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 / \
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

# initial parameters
N = 512                                     # number of particles
T_star = 0.8                                # temperature
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
nsteps = 100000
cycle_min = 10                              # minimum size of cycles

# data arrays for plotting
data_all = []
data_cut = []

# intialization of particle path lists
positions = {}
filename = 'boson_configuration.txt'
if os.path.isfile(filename):
    # read from file for intial configuration
    f = open(filename, 'r')
    for line in f:
        # reads the line in file f into list 'a'
        a = line.split()
        positions[tuple([float(a[0]), float(a[1]), float(a[2])])] = \
               tuple([float(a[3]), float(a[4]), float(a[5])])
    f.close()
    if len(positions) != N: exit('error input file')
    print 'starting from file', filename
else:
    # otherwise 'start from scratch'
    for k in range(N):
        a = levy_harmonic_path(1, beta)
        positions[a[0]] = a[0]
    print 'starting from scratch', filename

# sampling section
for step in range(nsteps):
    # choose a random particle and its path
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    # compute permutation cycle
    while True:
        # 'move' bosons from the main list to the perm_cycle list for inspection
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)   
        # this loop should only break if no more of the cycle is discovered
        if boson_b == perm_cycle[0]: break
        else: boson_a = boson_b
    k = len(perm_cycle)
    # taking data for plotting purposes
    data_all.append(perm_cycle[0][0])
    if k > cycle_min:
           data_cut.append(perm_cycle[0][0])
    # resample entire cycle
    perm_cycle = levy_harmonic_path(k, beta)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
    # choose particle paths for exchange
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm(a_1, b_2, beta) * rho_harm(a_2, b_1, beta)
    weight_old = rho_harm(a_1, b_1, beta) * rho_harm(a_2, b_2, beta)
    # position permutation accepted with metropolis rate, continue with exchange
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2

# saving current 'positions' for later reuse
f = open(filename, 'w')
for a in positions:
   b = positions[a]
   f.write(str(a[0]) + '    ' + str(a[1]) + '   ' + str(a[2]) + '   ' +  
           str(b[0]) + '    ' + str(b[1]) + '   ' + str(b[2]) + '\n')
f.close()

# histogram plotting
pylab.title('Probability Distribution for Particles in a Harmonic Well')
pylab.hist(data_all, bins=100, normed=True, alpha=0.8, label='All cyles')
pylab.hist(data_cut, bins=50, normed=True, alpha=0.5, \
    label='Cycles of length >{0}'.format(cycle_min))
t = [float(i)/10000 for i in range(-30000,30001)]
f_t = [math.exp(-a**2)/math.sqrt(math.pi) for a in t]
pylab.plot(t, f_t, label='$\\psi^2(x)$')  # analytic solution
pylab.xlim(-3.0,3.0)
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$')
pylab.legend()
pylab.savefig('markov_harmonic_bosons_hist.png')