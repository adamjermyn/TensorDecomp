import numpy as np
from benchmark import benchmark

import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')



def gg(x,y):
	return 1/(np.abs(np.subtract.outer(y,alpha*x))+1)

def keff(n, d, size):
	roots = np.roots([d-1, 0, d * n, -size])
	roots = roots[np.imag(roots) == 0]
	roots = roots[roots > 0]
	return np.real(roots[0])

d = 8
si = np.array(np.meshgrid(*[[0,1] for _ in range(d)], indexing='ij'))
l = np.tensordot(2**np.arange(d), si, axes=((0,),(0,)))
xi = l * (2 / 2**d) - 1

alphas = [0, 0.25, 0.5, 0.75, 1.0]

dataB = []
dataG = []

for alpha in alphas:
	x = gg(xi, xi)

	print(x.shape)


	dt, g = benchmark(greedy.findBest, x, 1e-18)
	dataG.append([alpha,sum([v.size for v in g]), keff(2,2*d,sum([v.size for v in g]))])

dataG = np.array(dataG)
dataB = np.array(dataB)

print(dataG)
print(dataB)
