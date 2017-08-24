import numpy as np

x = np.zeros((4,4,4,4))
for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				x[i,j,k,l] = np.exp(i*j + k*l)

import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig = plt.figure(figsize=(5,4))
ax = plt.subplot(111)

x1 = np.reshape(x, (16,16))
u, s, v = np.linalg.svd(x1)
plt.plot(s, label='(ij)(kl)')
print(s)

x2 = np.swapaxes(x, 1, 2)
x2 = np.reshape(x2, (16,16))
u, s, v = np.linalg.svd(x2)
plt.plot(s, label='(ik)(jl)')
print(s)

x2 = np.swapaxes(x, 1, 3)
x2 = np.reshape(x2, (16,16))
u, s, v = np.linalg.svd(x2)
plt.plot(s, label='(il)(jk)')
print(s)

ax.set_yscale('log')

plt.xlabel('Sorted Order')
plt.ylabel('Singular Value')
plt.legend()
ax.set_ylim([1e-10,1e8])
plt.tight_layout()
plt.savefig('svd.pdf')

