import numpy as np
from splitter import split

def findBest(tensor, threshold):
	t = np.copy(tensor)
	best = [1e100, None]
	for i in range(len(tensor.shape) - 1):
		for j in range(i + 1, len(t.shape)):
			u,s,v,vs = split(t, (i,j), threshold)
			if len(s) < best[0]:
				best = [len(s), u, vs]
	best = best[1:]
	if len(best[-1].shape) > 3:
		best = best[:-1] + findBest(best[-1], threshold)
	return best
