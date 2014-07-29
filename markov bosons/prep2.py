import random, pylab

data = []
for run in range(100000):
    data.append(random.uniform(0.0, 1.0))
pylab.title('Preparation program 2, SMAC week 7, 2014')
pylab.hist(data, bins=200, range=[0.5, 0.6], normed=True)
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$')
pylab.show()