import random, math

def Vol_s(dimension,r):
    return math.pi ** (dimension / 2.0)* r ** dimension/ math.gamma(dimension / 2.0 + 1.0)

for dimension in range(1,20):
    print dimension, Vol1_s(dimension)