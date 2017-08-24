import numpy as np

def split(tensor, indices, threshold):
	'''
	This method splits the given tensor into an object of the form

	A_{ijk} B_{k,...}

	and truncates the SVD according to the relative error threshold.
	Here i and j are the given indices and k is the new internal index.
	'''

	indices = list(indices)
	perm = list(range(len(tensor.shape)))
	perm.remove(indices[0])
	perm.remove(indices[1])
	perm = indices + perm
	t = np.transpose(tensor, axes=perm)
	arr = np.reshape(t, (t.shape[0]*t.shape[1], np.product(t.shape[2:])))

	u, s, v = np.linalg.svd(arr, full_matrices=False)
	
	p = s**2 / np.sum(s**2)

	s = s[p > threshold]
	u = u[:,p > threshold]
	v = v[p > threshold]

	vs = np.dot(np.diag(s), v)

	u = np.reshape(u, (t.shape[0], t.shape[1], len(s)))
	v = np.reshape(v, [len(s)] + list(t.shape[2:]))
	vs = np.reshape(vs, [len(s)] + list(t.shape[2:]))

	return u, s, v, vs

