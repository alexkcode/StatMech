import random, math

def Vol1_s(dimension):
    return math.pi ** (dimension / 2.0)/ math.gamma(dimension / 2.0 + 1.0)

for dimension in range(1,20):
    print dimension, Vol1_s(dimension)