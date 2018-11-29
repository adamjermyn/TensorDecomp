import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

### First Ising Test

dataB = np.loadtxt('../Data/isingDecomp1b.dat')
dataG = np.loadtxt('../Data/isingDecomp1g.dat')

fig = plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plt.plot(dataG[:,0],dataG[:,1], label='Greedy')
plt.plot(dataB[:,0], dataB[:,1], label='Brute force')
plt.yscale('log')
plt.xlabel('Number of Indices')
plt.ylabel('Compression Ratio')
plt.legend(loc="best")

ax = plt.subplot(212)
plt.plot(dataG[:,0],dataG[:,2], label='Greedy')
plt.plot(dataB[:,0], dataB[:,2], label='Brute force')
plt.yscale('log')
plt.xlabel('Number of Indices')
plt.ylabel('Time (s)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('ising.pdf')


### Second Ising Test

dataB = np.loadtxt('../Data/isingDecomp2b.dat')
dataG = np.loadtxt('../Data/isingDecomp2g.dat')

fig = plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plt.plot(dataG[:,0],dataG[:,1], label='Greedy')
plt.plot(dataB[:,0], dataB[:,1], label='Brute force')
plt.xlabel('J')
plt.ylabel('Compression Ratio')
plt.legend(loc="best")

ax = plt.subplot(212)
plt.plot(dataG[:,0],dataG[:,2], label='Greedy')
plt.plot(dataB[:,0], dataB[:,2], label='Brute force')
plt.yscale('log')
plt.xlabel('J')
plt.ylabel('Time (s)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('isingJ.pdf')

### Ising 2D Test

dataB = np.loadtxt('../Data/isingDecomp2Db.dat')
dataG = np.loadtxt('../Data/isingDecomp2Dg.dat')
dataG2 = np.loadtxt('../Data/isingDecomp2Dg2.dat')

fig = plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plt.plot(dataG[:,0],dataG[:,1], label='Greedy')
plt.plot(dataG2[:,0],dataG2[:,1], label='Greedy (Variable)')
plt.plot(dataB[:,0], dataB[:,1], label='Brute force')
plt.xlabel('J')
plt.ylabel('Compression Ratio')
plt.legend(loc="best")

ax = plt.subplot(212)
plt.plot(dataG[:,0],dataG[:,2], label='Greedy')
plt.plot(dataG2[:,0],dataG2[:,2], label='Greedy (Variable)')
plt.plot(dataB[:,0], dataB[:,2], label='Brute force')
plt.yscale('log')
plt.xlabel('J')
plt.ylabel('Time (s)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('isingJ2D.pdf')

### Sparse Test

dataB = np.loadtxt('../Data/isingDecompSparseB.dat')
dataG = np.loadtxt('../Data/isingDecompSparseG.dat')

fig = plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plt.plot(dataG[:,0],dataG[:,1], label='Greedy')
plt.plot(dataB[:,0], dataB[:,1], label='Brute force')
plt.yscale('log')
plt.xlabel('Number of Indices')
plt.ylabel('Compression Ratio')
plt.legend(loc="best")

ax = plt.subplot(212)
plt.plot(dataG[:,0],dataG[:,2], label='Greedy')
plt.plot(dataB[:,0], dataB[:,2], label='Brute force')
plt.yscale('log')
plt.xlabel('Number of Indices')
plt.ylabel('Time (s)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('sparse.pdf')

