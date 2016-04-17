from math import *

def b2(i):
    return ((log2(i) + log2(log2(i))) * log2(i))**2

#for j in range(127000, 128000, 1):
for j in range(2, 40):
    print(j, b2(j), j > b2(j))
