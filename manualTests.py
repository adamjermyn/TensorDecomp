import numpy as np
import brute
import greedy

## Manual example

x = np.zeros((4,4,4,4))
for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				x[i,j,k,l] = np.exp(i*j + k*l)

print('Manual Test:')
print([v.shape for v in brute.findBest(x, 1e-6)[2]])
print([v.shape for v in greedy.findBest(x, 1e-6)])
print('---')

x = np.zeros((4,4,4,4,4))
for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				for m in range(4):
					x[i,j,k,l,m] = np.exp(i*j + k*l + m)

print('Manual Test:')
print([v.shape for v in brute.findBest(x, 1e-6)[2]])
print([v.shape for v in greedy.findBest(x, 1e-6)])
print('---')

x = np.zeros((4,4,4,4,4))
for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				for m in range(4):
					x[i,j,k,l,m] = np.exp(i*j + k*l + m) + np.sin(i*j)*np.cos(k*l)*np.tanh(m)

print('Manual Test:')
print([v.shape for v in brute.findBest(x, 1e-6)[2]])
print([v.shape for v in greedy.findBest(x, 1e-6)])
print('---')
