import numpy as np
import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


dataB = []
dataG = []

n = 9
jran = np.linspace(-5,5,num=30,endpoint=True)
for J in jran:
	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)
	x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

	print(x.shape)

	b = brute.findBest(x, 1e-6)
	g = greedy.findBest(x, 1e-6)


	dataB.append(sum([v.size for v in b[2]]) * 1./x.size)
	dataG.append(sum([v.size for v in g]) * 1./x.size)

fig = plt.figure(figsize=(5,4))
ax = plt.subplot(111)
plt.plot(jran, dataB, label='Brute force')
plt.plot(jran, dataG, label='Greedy')
plt.xlabel('J')
plt.ylabel('Compression Ratio')
plt.legend()
plt.tight_layout()
plt.savefig('../isingJ.pdf')
