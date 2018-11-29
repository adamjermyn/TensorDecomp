import numpy as np
import time

import brute
import greedy
import greedy_variable

dataB = []
dataG = []
dataG2 = []

n = 9
jran = np.linspace(-7,7,num=100,endpoint=True)

for J in jran:

	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)

	x = np.exp(-J*(si[0]*si[1] + si[1]*si[2] + si[0]*si[3] + si[1]*si[4] + si[2]*si[5] + si[3]*si[4] + si[4]*si[5] + si[3]*si[6] + si[4]*si[7] + si[5]*si[8] + si[6]*si[7] + si[7]*si[8]))

	print(x.shape)

	start = time.clock()
	b = brute.findBest(x, 1e-6)
	end = time.clock()
	dataB.append([J,sum([v.size for v in b[2]]) * 1./x.size, end - start])


	start = time.clock()
	g = greedy.findBest(x, 1e-6)
	end = time.clock()
	dataG.append([J,sum([v.size for v in g]) * 1./x.size, end - start])


	start = time.clock()
	g2 = greedy_variable.findBest(x, 1e-6)
	end = time.clock()
	dataG2.append([J,sum([v.size for v in g2]) * 1./x.size, end - start])


	print([a.shape for a in b[2]])
	print([a.shape for a in g])
	print(sum([v.size for v in g]))


np.savetxt('../Data/isingDecomp2Db.dat', dataB)
np.savetxt('../Data/isingDecomp2Dg.dat', dataG)
np.savetxt('../Data/isingDecomp2Dg2.dat', dataG2)
