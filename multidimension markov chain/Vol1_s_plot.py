import random, math, pylab

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

N = 200
vol = []

for i in range(N):
	vol.append(Vol1_s(i))

pylab.plot(range(N), vol, '+')
pylab.gca().set_yscale('log')
pylab.xlabel('Dimension')
pylab.ylabel('Volume')
pylab.title('Unit Hypersphere Volume vs. Dimension')
pylab.savefig('vol1_s_plot.png')
pylab.show()

print(Vol1_s(5), Vol1_s(20), Vol1_s(200))