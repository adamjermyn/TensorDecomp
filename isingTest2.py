import numpy as np
import time

import brute
import greedy

dataB = []
dataG = []

n = 9
jran = np.linspace(-5,5,num=30,endpoint=True)
for J in jran:
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	start = time.clock()
	b = brute.findBest(x, 1e-6)
	end = time.clock()
	dataB.append([J,sum([v.size for v in b[2]]) * 1./x.size, end - start])


	start = time.clock()
	g = greedy.findBest(x, 1e-6)
	end = time.clock()
	dataG.append([J,sum([v.size for v in g]) * 1./x.size, end - start])


np.savetxt('../Data/isingDecomp2b.dat', dataB)
np.savetxt('../Data/isingDecomp2g.dat', dataG)

