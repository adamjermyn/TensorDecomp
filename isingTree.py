import numpy as np
import brute
import greedy

import matplotlib.pyplot as plt
plt.style.use('ggplot')


dataB = []
dataG = []

n = 9
J = 1
	
si = np.array(np.meshgrid(*[[0,1] for _ in range(n)], indexing='ij'))
print(si.shape)
x = np.exp(-J*np.sum(si[:-1]*si[1:], axis=0))

print(x.shape)

b = brute.findBest(x, 1e-6)
g = greedy.findBest(x, 1e-6)


print(b[1])

