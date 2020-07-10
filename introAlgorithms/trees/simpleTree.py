'''
A tree whose node is impleted by a linked list.
Not have any special properties. Should NOT be used for any purpose.
Built as a first attempt to build a binary tree.
'''

def iterate_tree (N, A):
	'''
	Running time = O (n) with n = len (T)
	'''
	A.append (N.key ())
	child = T.left ()
	sibling = T.right ()
	if child:
		iterate_tree (child, A)
	if sibling:
		iterate_tree (sibling, A)

def iterate_tree2 (N):
	A = []
	stack = [N]
	while len (stack):
		n = stack.pop ()
		A.append (n.key ())
		c = n.left ()
		s = n.right ()
		if c: stack.insert (0, c)
		if s: stack.insert (0, s)
	return A

class Node:
	def __init__ (self, key, top=None, left=None, right=None):
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
		Return the leftmost child
		'''
		return self._left

	def right (self):
		'''
		Return the immediate to-the-right sibling
		'''
		return self._right

	def top (self):
		'''
		Return the parent
		'''
		return self._top


