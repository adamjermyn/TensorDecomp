import numpy as np
from benchmark import benchmark

import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


dataB = []
dataG = []


J = 1.0

for n in range(4,11):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	dt, b = benchmark(brute.findBest, x, 1e-6)
	dataB.append([n,sum([v.size for v in b[2]]) * 1./x.size, dt])

	dt, g = benchmark(greedy.findBest, x, 1e-6)
	dataG.append([n,sum([v.size for v in g]) * 1./x.size, dt])

for n in range(11,17):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	dt, g = benchmark(greedy.findBest, x, 1e-6)
	dataG.append([n,sum([v.size for v in g]) * 1./x.size, dt])


np.savetxt('../Data/isingDecomp1b.dat', dataB)
np.savetxt('../Data/isingDecomp1g.dat', dataG)
