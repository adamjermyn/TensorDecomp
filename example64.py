import numpy as np
from benchmark import benchmark

import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


alpha = 0.5

def gg(x,y):
	return 1/(np.abs(np.subtract.outer(y,alpha*x))+1)

def keff(n, d, size):
	roots = np.roots([d-1, 0, d * n, -size])
	roots = roots[np.imag(roots) == 0]
	roots = roots[roots > 0]
	return np.real(roots[0])

dataB = []
dataG = []


J = 1.0

for d in range(2,5):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(d)], indexing='ij'))
	l = np.tensordot(2**np.arange(d), si, axes=((0,),(0,)))
	xi = l * (2 / 2**d) - 1

	x = gg(xi, xi)

	dt, b = benchmark(brute.findBest, x, 1e-8)
	dataB.append([d,keff(2,2*d,sum([v.size for v in b[2]])),sum([v.size for v in b[2]]) * 1./x.size, dt])

	dt, g = benchmark(greedy.findBest, x, 1e-8)
	dataG.append([d,keff(2,2*d,sum([v.size for v in g])),sum([v.size for v in g]) * 1./x.size, dt])

	print(d, dataB[-1][1], dataG[-1][1])


for d in range(5,8):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(d)], indexing='ij'))
	l = np.tensordot(2**np.arange(d), si, axes=((0,),(0,)))
	xi = l * (2 / 2**d) - 1

	x = gg(xi, xi)

	dt, g = benchmark(greedy.findBest, x, 1e-8)
	dataG.append([d,keff(2,2*d,sum([v.size for v in g])),sum([v.size for v in g]) * 1./x.size, dt])

	print(d, dataG[-1][1])


print(dataB)
print(dataG)

np.savetxt('../Data/e64Decomp1b.dat', dataB)
np.savetxt('../Data/e64Decomp1g.dat', dataG)
