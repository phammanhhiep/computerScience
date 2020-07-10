import os, sys
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from trees.redBlackTree import left_rotate, right_rotate, Node2 as Node, _tree_insert, tree_insert, insert_fixup

@pytest.fixture
def atree ():
	root = Node (15)
	n1 = Node (6, top=root)
	n2 = Node (18, top=root)
	n3 = Node (3, top=n1)
	n4 = Node (7, top=n1)
	n5 = Node (17, top=n2)	

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	T = {'root': root}
	return T	

@pytest.fixture
def atree2 ():
	root = Node (key=11, color=Node.BLACK)
	n1 = Node (key=2, color=Node.RED, top=root)
	n2 = Node (key=14, color=Node.BLACK, top=root)
	n3 = Node (key=1, color=Node.BLACK, top=n1)
	n4 = Node (key=7, color=Node.BLACK, top=n1)
	n5 = Node (key=15, color=Node.RED, top=n2)
	n6 = Node (key=5, color=Node.RED, top=n4)
	n7 = Node (key=8, color=Node.RED, top=n4)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._right = n5
	n4._left = n6
	n4._right = n7

	T = {'root': root}
	return T	

@pytest.mark.skip
def test_left_rotate (atree):
	root = atree['root']
	left_rotate (atree, root)
	new_root = atree['root']
	assert new_root.key () == 18
	assert new_root.right () is None
	assert new_root.left () == root
	assert root.right ().key () == 17 

@pytest.mark.skip
def test_right_rotate (atree):
	root = atree['root']
	right_rotate (atree, root)
	new_root = atree['root']
	assert new_root.key () == 6
	assert new_root.right () == root
	assert new_root.left ().key () == 3
	assert root.left ().key () == 7 

@pytest.mark.skip
def test__tree_insert (atree2):

	n = Node (key=4, color=Node.RED)
	_tree_insert (atree2, n)

	assert n.color () == Node.RED
	assert n.top ().key () == 5
	assert n.left () is None
	assert n.right () is None

@pytest.mark.skip
def test_insert_fixup (atree2):
	pass

@pytest.mark.skip
def test_insert_fixup1 ():
	'''
	Case 1: z and z's parent, and z's uncle are red
	'''
	root = Node (key=7, color=Node.BLACK)
	n1 = Node (key=5, color=Node.RED, top=root)
	n2 = Node (key=8, color=Node.RED, top=root)
	n3 = Node (key=4, color=Node.RED, top=n1)

	root._left = n1
	root._right = n2
	n1._left = n3

	T = {'root': root}

	insert_fixup (T, n3)

	assert root.color () == Node.BLACK
	assert root.left () == n1
	assert root.right () == n2
	assert n1.color () == Node.BLACK
	assert n2.color () == Node.BLACK
	assert n3.color () == Node.RED

@pytest.mark.skip
def test_insert_fixup2 ():
	'''
	Case 2 & 3: z and z's parent, and z's uncle are black
	z's parent is on the left of z's grandparent
	'''
	root = Node (key=11, color=Node.BLACK)
	n1 = Node (key=2, color=Node.RED, top=root)
	n2 = Node (key=14, color=Node.BLACK, top=root)
	n3 = Node (key=1, color=Node.BLACK, top=n1)
	n4 = Node (key=7, color=Node.RED, top=n1)
	n5 = Node (key=15, color=Node.RED, top=n2)
	n6 = Node (key=5, color=Node.BLACK, top=n4)
	n7 = Node (key=8, color=Node.BLACK, top=n4)
	n8 = Node (key=4, color=Node.RED, top=n5)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._right = n5
	n4._left = n6
	n4._right = n7
	n5._left = n8

	T = {'root': root}
	
	insert_fixup (T, n4)

	assert n4.top () is None
	assert n4.color () == Node.BLACK
	assert root.color () == Node.RED
	assert root.top () == n4
	assert root.left () == n7
	assert n1.top () == n4
	assert n1.right () == n6

# @pytest.mark.skip
def test_insert_fixup3 ():
	'''
	Case 2 & 3: z and z's parent, and z's uncle are black
	z's parent is on the right of z's grandparent	
	'''
	root = Node (key=10, color=Node.BLACK)
	n1 = Node (key=2, color=Node.BLACK, top=root)
	n2 = Node (key=14, color=Node.RED, top=root)
	n3 = Node (key=12, color=Node.RED, top=n2)
	n4 = Node (key=15, color=Node.BLACK, top=n2)
	n5 = Node (key=1, color=Node.RED, top=n1)
	n6 = Node (key=11, color=Node.BLACK, top=n3)
	n7 = Node (key=13, color=Node.BLACK, top=n3)

	root._left = n1
	root._right = n2
	n1._left = n5
	n2._left = n3
	n2._right = n4
	n3._left = n6
	n3._right = n7

	T = {'root': root}
	
	insert_fixup (T, n3)

	assert n3.top () is None
	assert n3.color () == Node.BLACK
	assert root.color () == Node.RED
	assert root.top () == n3
	assert root.right () == n6
	assert n2.top () == n3
	assert n2.left () == n7