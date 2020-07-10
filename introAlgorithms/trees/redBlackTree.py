import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from trees.binarySearchTree import Node

def left_rotate (T, n):
	r = n.right ()
	if r is None:
		raise ValueError ('Right node should not be None.')
	r._top = n.top ()
	if n.top () is None:
		T['root'] = r
	elif n.top ().left () == n:
		n.top ()._left = r
	else:
		n.top ()._right = r

	n._top = r
	n._right = r.left ()
	r._left = n

def right_rotate (T, n):
	l = n.left ()
	if l is None:
		raise ValueError ('Left node should not be None.')
	l._top = n.top ()
	if n.top () is None:
		T['root'] = l
	elif n.top ().left () == n:
		n.top ()._left = l
	else:
		n.top ()._right = l
	
	n._top = l
	n._left = l.right ()
	l._right = n

def insert_fixup (T, n):
	'''
	Maintain the properties of a red-black tree.
	Due to invariant loop, only one of the two properties are are being violated at the beginning of any iteration: 
		+ Root is red
		+ Children of a red node are not all black.
	'''
	while n.top () and n.top ().color () is n.RED:
		p = n.top ()
		g = p.top ()
		if p is g.left ():

			u = g.right ()
			if u.color () is n.RED:
				g._color = n.RED
				u._color = n.BLACK
				p._color = n.BLACK
				n = g
			else:
				if n is p.right ():
					n = p
					left_rotate (T, n)
				p = n.top ()
				g = p.top ()
				p._color = n.BLACK
				g._color = n.RED
				right_rotate (T, g)
		else:
			u = g.left ()
			if u.color () is n.RED:
				g._color = n.RED
				p._color = n.BLACK
				u._color = n.BLACK
				n = g
			else:
				if n is p.left ():
					n = p
					right_rotate (T, n)
				p = n.top ()
				g = p.top ()	
				p._color = n.BLACK
				g._color = n.RED
				left_rotate (T, g)

	T['root']._color = Node2.BLACK

def _tree_insert (T, n):
	r = T['root']
	p = None
	while r is not None:
		p = r
		if r.key () >= n.key ():
			r = r.left ()
		else:
			r = r.right ()
	if p is None:
		T['root'] = n
	elif p.key () >= n.key ():
		p._left = n
	else:
		p._right = n
	n._top = p
	n.set_color (n.RED)	

def tree_insert (T, n):
	_tree_insert (T,n)
	insert_fixup (T, n)


def tree_delete (T, n): pass

class Node2 (Node):
	RED = 1
	BLACK = 2	
	def __init__ (self, key=None, top=None, left=None, right=None, color=None):
		Node.__init__ (self, key, top, left, right)
		self._color = color

	def color (self):
		return self._color

	def set_color (self, color):
		if color not in [self.RED, self.BLACK]:
			raise ValueError ('Color is not valid.')
		self._color = color