def inorder_tree_walk (x, A):
	'''
	Recursive version
	'''
	if x is not None:
		inorder_tree_walk (x.left (), A)
		A.append (x.key ())
		inorder_tree_walk (x.right (), A)

def inorder_tree_walk2 (x, A):
	'''
	Nonrecursive version
	'''

def inorder_tree_walk3 (x, A):
	'''
	Use tree_min and tree_successor.
	'''
	m = tree_min (x)
	A.append (m.key ())
	s = tree_successor (m)
	while s is not None:
		A.append (s.key ())
		s = tree_successor (s)
	return A

def tree_search (x, y):
	'''
	Recursive version
	'''
	if x is None or x.key () == y:
		return x
	if x.key () > y:
		return tree_search (x.left (), y)
	elif x.key () < y:
		return tree_search (x.right (), y)

def tree_search2 (x, y):
	'''
	Iterative version
	'''
	while x is not None and x.key () != y:
		if x.key () > y:
			x = x.left ()
		elif x.key () < y:
			x = x.right ()
	return x

def tree_min (x):
	if x.left () is not None:
		return tree_min (x.left ())
	return x

def tree_max (x):
	if x.right () is not None:
		return tree_max (x.right ())
	return x

def tree_successor (x):
	if x.right ():
		return tree_min (x.right ())
	p = x.top ()
	while p is not None and p.left () != x:
		x = p
		p = x.top ()
	return p 

def tree_predecessor (x):
	if x.left ():
		return tree_max (x.left ())
	p = x.top ()
	while p is not None and p.right () != x:
		x = p
		p = x.top ()
	return p

def preorder_tree_walk (x, A): pass

def postorder_tree_walk (x, A): pass

def tree_insert (T, x):
	'''
	Assume T is a node and is not None.
	::param T:: T is a node. 
	'''
	if T.key () >= x.key ():
		if T.left ():
			tree_insert (T.left (), x)
		else:
			T._left = x
			x._top = T
	elif T.key () < x.key ():
		if T.right ():
			tree_insert (T.right (), x)
		else:
			T._right = x
			x._top = T

def tree_insert2 (T, x):
	'''
	Build a tree from scratch. 
	::param T:: T is a tree.
	::param x:: x is a node without root, left, and right.
	'''
	y = T['root']
	p = None
	while y is not None:
		p = y
		if y.key () <= x.key ():
			y = y.right ()
		else:
			y = y.left ()
	x._top = p
	if p is None:
		T['root'] = x
	elif x.key () <= p.key ():
		p._left = x
	else:
		p._right = x

def tree_delete (T, x):
	'''
	Running time is O of n
	'''
	if x.left () is None:
		transplant (T, x, x.right ())
	elif x.right () is None:
		transplant (T, x, x.left ())
	else:
		successor = tree_successor (x)
		if successor.right ():
			tree_delete (T, successor)
		transplant (T, x, successor)
		successor._left = x.left ()
		successor._right = x.right ()

def transplant (T, u, v):
	if u.top () is None:
		T['root'] = v
	else:
		if v is not None:
			v._top = u.top ()
	if u.top ().left () == u:
		u.top ()._left = v
	else:
		u.top ()._right = v

class Node:
	def __init__ (self, key=None, top=None, left=None, right=None):
		self._key = key
		self._top = top
		self._left = left
		self._right = right

	def key (self):
		'''
		Return the key of a node
		'''
		return self._key

	def left (self):
		'''
		Return the left child
		'''
		return self._left

	def right (self):
		'''
		Return the right child
		'''
		return self._right

	def top (self):
		'''
		Return the parent
		'''
		return self._top

	def set_left (self): pass

	def set_right (self): pass

	def set_top (self): pass

	def set_key (self): pass