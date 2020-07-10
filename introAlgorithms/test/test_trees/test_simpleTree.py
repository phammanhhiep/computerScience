import os, sys
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from trees.simpleTree import iterate_tree2, iterate_tree, Node

def test_iterate_tree (): pass

def test_iterate_tree2 ():
	root = Node (0)
	n1 = Node (1, top=root)
	n2 = Node (2, top=root)
	n3 = Node (3, top=n1)
	n4 = Node (4, top=n1)
	n5 = Node (5, top=n2)

	root._left = n1
	n1._left = n3
	n1._right = n2
	n2._left = n5
	n3._right = n4

	A = iterate_tree2 (root)

	E = [0,1,3,2,4,5]

	assert len (A) == len (E)
	for i in range (len (A)):
		assert A[i] == E[i]