import numpy as np
import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


dataB = []
dataG = []

n = 9
jran = np.linspace(-7,7,num=30,endpoint=True)

#jran = [jran[-3]]

for J in jran:

	si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
	print(si.shape)

	x = np.exp(-J*(si[0]*si[1] + si[1]*si[2] + si[0]*si[3] + si[1]*si[4] + si[2]*si[5] + si[3]*si[4] + si[4]*si[5] + si[3]*si[6] + si[4]*si[7] + si[5]*si[8] + si[6]*si[7] + si[7]*si[8]))

	print(x.shape)

	b = brute.findBest(x, 1e-6)
	g = greedy.findBest(x, 1e-6)

	print([a.shape for a in b[2]])
	print([a.shape for a in g])
	print(sum([v.size for v in g]))

	dataB.append(sum([v.size for v in b[2]]) * 1./x.size)
	dataG.append(sum([v.size for v in g]) * 1./x.size)

fig = plt.figure(figsize=(5,4))
ax = plt.subplot(111)
print(dataB)
print(dataG)
plt.plot(jran, dataB, label='Brute force')
plt.plot(jran, dataG, label='Greedy')
plt.xlabel('J')
plt.ylabel('Compression Ratio')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('../isingJ2D.pdf')
