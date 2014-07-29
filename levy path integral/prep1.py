#
# Part one
#
print 'Part 1'
L = range(10)
for k in range(10):
    print L
    L = L[3:] + L[:3]
print
#
# Part two 
#
print 'Part 2'
K = range(10)
for i in range(10):
    print K
    dummy = K.pop()
    K = [dummy] + K
print
#
# Part three
#
print 'Part 3'
J = range(10)
for i in range(10):
    print K
    dummy = K.pop(0)
    K = K + [dummy]
print
#
# Part four
#
print 'Part 4'
I = range(10)
weight = sum(a ** 2 for a in I)
print weight