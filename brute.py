import numpy as np
from splitter import split
from tree_enum import constructTrees, treeToSplit

def findBest(tensor, threshold):
	best = [1e100, None]
	trees = constructTrees(len(tensor.shape))
	print(len(trees))

	for i,t in enumerate(trees):
		if i%50 == 0:
			print(i, len(trees))
		v = np.copy(tensor)
		s = treeToSplit(t)
		arrs = []
		for indices in s:
			u,s,v,vs = split(v, indices, threshold)
			arrs.append(u)
			if len(v.shape) == 3:
				arrs.append(vs)
		if sum([a.size for a in arrs]) < best[0]:
			best = [sum([a.size for a in arrs]), t, arrs]

	return best



