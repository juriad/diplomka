from math import *
from pylab import *

def size(n, v, b):
    return 2**(b(n) + ceil(log2(b(n)))) * ceil(log2(b(n)+1)), ceil(n/b(n)) * ceil(log2(v(n)+1)), ceil(n/v(n)) * ceil(log2(n+1))

for i in range(0, 41, 5):
    #bf = lambda n: ceil(log2(n) * 0.5)
    bf = lambda n: 64
    vf = lambda n: ceil(log2(n)) ** 2 /5
    n = 2**i
    b, v, m = size(n, vf, bf)
    print(i, log2(b/n), log2(v/n), log2(m/n), log2((b+v+m)/n))
