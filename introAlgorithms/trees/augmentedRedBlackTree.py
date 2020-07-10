import os, sys
sys.path.insert (0, os.path.abspath ('./'))

from trees.binarySearchTree import Node

def os_select (N, i):
	'''
	Return a node whose rank is i. The node has i-th smallest key in the subtree.
	::param N:: red-black tree, having size information
	::param i:: the ranking of a node
	'''
	rank = N.left ().size () + 1
	if rank == i:
		return N
	elif rank > i:
		return os_select (N.left (), i)
	else:
		return os_select (N.right (), i - rank)

def os_rank (R, N):
	'''
	::param R:: root of a red-black tree.
	::param N:: a node.
	'''
	rank = 1 if N.left () is None else (N.left ().size () + 1)
	y = N

	while y != R:
		if y.top ().right () == y:
			rank += y.top ().left ().size () + 1
		y = y.top ()
	return rank


class Node2 (Node):
	def __init__ (self, key=None, top=None, left=None, right=None, size=None):
		Node.__init__ (self, key, top, left, right)
		self._size = size

	def size (self):
		return self._size

