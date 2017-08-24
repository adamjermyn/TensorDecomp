'''
For our purposes a valid tree is written as a set

(A,B,C)

where each of A, B, C may be themselves sets of objects.
The top-level tuple contains a triplet and all lower levels
contain just pairs.
'''

def addNode(tree, node):
	'''
	This method returns the result of inserting a node
	into a tree by constructing a new internal node in
	place of an edge and attaching the node to that edge.
	What this means is that we replace an object at some
	level in the tree with the set containing that object
	and the new node.
	
	The result is returned for all possible insertion points.
	'''

	result = []

	for o in tree:
		newO = frozenset((o, node))
		newS = set(tree.difference(set([o])))
		newS.add(newO)
		tNew = frozenset(newS)
		result.append(tNew)

		# Now recurse
		try:
			res = addNode(o, node)
			for newO in res:
				newS = set(tree.difference(set([o])))
				newS.add(newO)
				tNew = frozenset(newS)
				result.append(tNew)
		except:
			res = None			
	
	return result

def constructTrees(num):
	'''
	This returns all unrooted binary trees with precisely n leaves.
	The leaves are numbered from 0 to num - 1 inclusive.
	'''
	if num == 1:
		return frozenset([0])
	elif num == 2:
		return frozenset([0,1])
	else:
		result = [frozenset((0,1,2))]

		for i in range(3, num):
			result = [addNode(t, i) for t in result] # Add a node
			result = [r for res in result for r in res] # Flatten

		return result

def findPair(tree):
	'''
	This method searches a tree and returns the first frozenset it finds containing two non-iterable objects.
	'''
	for o in tree:
		if isinstance(o, frozenset):
			if len(o) == 2:
				oList = list(o)
				if not isinstance(oList[0], frozenset) and not isinstance(oList[1], frozenset):
					return o
				else:
					if findPair(o) is not None:
						return findPair(o)
	return None				


def removePair(tree, inds):
	'''
	This constructs a copy of a tree with the specified indices removed and replaced by a new index at the start.
	'''
	t = set()

	for o in tree:
		if isinstance(o, frozenset):
			t.add(removePair(o, inds))
		else:
			if o in inds:
				t.add(0)
			elif o > inds[0] and o > inds[1]:
				t.add(o - 1)
			elif o > inds[0] or o > inds[1]:
				t.add(o)
			elif o < inds[0] and o < inds[1]:
				t.add(o + 1)
	
	if len(t) > 1:
		return frozenset(t)
	else:
		return list(t)[0]


def treeToSplit(tree):
	'''
	This turns a tree object into a set of instructions which may be passed to the splitter.
	These instructions take the form of a list of sets specifying pairs of indices to be split off.
	There are many different correct sets of instructions, and it only matters that we find one.
	Note that it is assumed that after splitting the new index always goes at the start.
	'''

	result = []

	pair = findPair(tree)
	if pair is not None:
		result.append(pair)
		result = result + treeToSplit(removePair(tree, list(pair)))

	return result

