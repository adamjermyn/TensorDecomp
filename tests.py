import numpy as np
import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')

## Random examples

print('Random Normal:')
print('---')

dataB = []
dataG = []

for n in range(4, 10):

	dB = []
	dG = []

	for _ in range(100):
		x = np.random.randn(*[2 for _ in range(n)])

		b = brute.findBest(x, 1e-6)
		g = greedy.findBest(x, 1e-6)



		dB.append(sum([v.size for v in b[2]]) * 1./x.size)
		dG.append(sum([v.size for v in g]) * 1./x.size)

	dataB.append(np.average(dB))
	dataG.append(np.average(dG))

for n in range(10,16):
	dG = []

	for _ in range(100):
		x = np.random.randn(*[2 for _ in range(n)])

		g = greedy.findBest(x, 1e-6)
		dG.append(sum([v.size for v in g]) * 1./x.size)

	dataG.append(np.average(dG))


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,4))
ax = plt.subplot(111)
plt.plot(range(4,10), dataB, label='Brute force')
plt.plot(range(4,16), dataG, label='Greedy')
plt.xlabel('Number of Indices')
plt.ylabel('Compression Ratio')
plt.legend()
plt.tight_layout()
plt.savefig('../normal.pdf')
