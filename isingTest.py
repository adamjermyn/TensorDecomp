import numpy as np
import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


dataB = []
dataG = []


J = 1.0

for n in range(4,10):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	b = brute.findBest(x, 1e-6)
	g = greedy.findBest(x, 1e-6)


	dataB.append(sum([v.size for v in b[2]]) * 1./x.size)
	dataG.append(sum([v.size for v in g]) * 1./x.size)

for n in range(10,15):
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	g = greedy.findBest(x, 1e-6)

	dataG.append(sum([v.size for v in g]) * 1./x.size)



fig = plt.figure(figsize=(5,4))
ax = plt.subplot(111)
plt.plot(range(4,15), dataG, label='Greedy')
plt.plot(range(4,10), dataB, label='Brute force')
plt.xlabel('Number of Indices')
plt.ylabel('Compression Ratio')
plt.legend()
plt.tight_layout()
plt.savefig('../ising.pdf')

