import numpy as np
import time

import brute
import greedy

## Random examples

print('Sparse Random Binary:')
print('---')

dataB = []
dataG = []

for n in range(4, 9):

	print(n)

	dB = []
	dG = []

	for _ in range(100):
		x = np.random.choice(2, size=[2 for k in range(n)], p=[0.95,0.05])
		while np.sum(x) == 0:
			x = np.random.choice(2, size=[2 for k in range(n)], p=[0.95,0.05])


		start = time.clock()
		b = brute.findBest(x, 1e-6)
		end = time.clock()
		dB.append([n,sum([v.size for v in b[2]]) * 1./x.size, end - start])


		start = time.clock()
		g = greedy.findBest(x, 1e-6)
		end = time.clock()
		dG.append([n,sum([v.size for v in g]) * 1./x.size, end - start])

	dataB.append(np.average(dB, axis=0))
	dataG.append(np.average(dG, axis=0))

for n in range(9,16):
	dG = []

	print(n)

	for _ in range(100):
		x = np.random.choice(2, size=[2 for k in range(n)], p=[0.95,0.05])
		while np.sum(x) == 0:
			x = np.random.choice(2, size=[2 for k in range(n)], p=[0.95,0.05])

		start = time.clock()
		g = greedy.findBest(x, 1e-6)
		end = time.clock()
		dG.append([n,sum([v.size for v in g]) * 1./x.size, end - start])

	dataG.append(np.average(dG, axis=0))


np.savetxt('Data/isingDecompSparseB.dat', dataB)
np.savetxt('Data/isingDecompSparseG.dat', dataG)
