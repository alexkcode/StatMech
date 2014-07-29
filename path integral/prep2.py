import numpy

a = numpy.array([[1,2,3],[4,5,6]])
b = numpy.array([[1,2],[3,4],[5,6]])
c = numpy.dot(a,b)
d = numpy.dot(b,a)
e = d * 2
f = numpy.diag(c)
g = numpy.diag(c).sum()

file = open('5.A2.txt', 'w')
file.write('c = ' + str(c) + '\n')
file.write('d = ' + str(d) + '\n')
file.write('e = ' + str(e) + '\n')
file.write('trace(c) = g = ' + str(g) + '\n')