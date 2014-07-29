Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'

for name in Names: print name, Names[name]

# checkpoint 1
print 'checkpoint 1\n'
a = Names.pop('Albert')
for name in Names: print name, Names[name]
print '\n'
# checkpoint 2
del Names['Richard']
print 'checkpoint 2\n'
for name in Names: print name, Names[name]
print '\n'
# checkpoint 3
L = Names.keys()
M = Names.values()
#checkpoint 4
print 'checkpoint 4\n'
b = 'Wolfgang' in Names
for name in Names: print name, Names[name]
print '\n'
#checkpoint 5
Names[1]=[1.0,2.0]