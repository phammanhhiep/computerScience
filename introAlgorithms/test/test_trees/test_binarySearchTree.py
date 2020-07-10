import os, sys
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from trees.binarySearchTree import Node, inorder_tree_walk, inorder_tree_walk3, tree_search, tree_search2, tree_min, tree_max, tree_successor, tree_predecessor, tree_insert, tree_insert2, transplant, tree_delete

@pytest.fixture
def atree ():
	root = Node (15)
	n1 = Node (6, top=root)
	n2 = Node (18, top=root)
	n3 = Node (3, top=n1)
	n4 = Node (7, top=n1)
	n5 = Node (17, top=n2)
	n6 = Node (20, top=n2)
	n7 = Node (2, top=n3)
	n8 = Node (4, top=n3)
	n9 = Node (13, top=n4)
	n10 = Node (9, top=n9)	

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5
	n2._right = n6
	n3._left = n7
	n3._right = n8
	n4._right = n9
	n9._left = n10

	T = {'root': root}
	return T	

@pytest.mark.skip
def test_inorder_tree_walk ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	A = []

	inorder_tree_walk (root, A)

	E = [12, 13, 15, 17, 18, 20]

	assert len (A) == len (E)
	for i in range (len (A)):
		assert A[i] == E[i]

@pytest.mark.skip
def test_inorder_tree_walk3 ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	A = []

	inorder_tree_walk3 (root, A)

	E = [12, 13, 15, 17, 18, 20]

	assert len (A) == len (E)
	for i in range (len (A)):
		assert A[i] == E[i]

@pytest.mark.skip
def test_tree_search ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	a = tree_search (root, 15)
	b = tree_search (root, 30)
	assert a.key () == 15
	assert b is None

@pytest.mark.skip
def test_tree_search2 ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	a = tree_search2 (root, 15)
	b = tree_search2 (root, 30)
	assert a.key () == 15
	assert b is None

@pytest.mark.skip
def test_tree_min ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	a = tree_min (root)
	assert a.key () == 12

@pytest.mark.skip
def test_tree_max ():
	root = Node (17)
	n1 = Node (13, top=root)
	n2 = Node (20, top=root)
	n3 = Node (12, top=n1)
	n4 = Node (15, top=n1)
	n5 = Node (18, top=n2)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5

	a = tree_max (root)
	assert a.key () == 20

@pytest.mark.skip
def test_tree_successor ():
	root = Node (15)
	n1 = Node (6, top=root)
	n2 = Node (18, top=root)
	n3 = Node (3, top=n1)
	n4 = Node (7, top=n1)
	n5 = Node (17, top=n2)
	n6 = Node (20, top=n2)
	n7 = Node (2, top=n3)
	n8 = Node (4, top=n3)
	n9 = Node (13, top=n4)
	n10 = Node (9, top=n9)	

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5
	n2._right = n6
	n3._left = n7
	n3._right = n8
	n4._right = n9
	n9._left = n10	

	a = tree_successor (root)
	assert a.key () == 17
	a = tree_successor (n9)
	assert a.key () == 15

@pytest.mark.skip
def test_tree_predecessor ():
	root = Node (15)
	n1 = Node (6, top=root)
	n2 = Node (18, top=root)
	n3 = Node (3, top=n1)
	n4 = Node (7, top=n1)
	n5 = Node (17, top=n2)
	n6 = Node (20, top=n2)
	n7 = Node (2, top=n3)
	n8 = Node (4, top=n3)
	n9 = Node (13, top=n4)
	n10 = Node (9, top=n9)	

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5
	n2._right = n6
	n3._left = n7
	n3._right = n8
	n4._right = n9
	n9._left = n10

	a = tree_predecessor (n1)
	assert a.key () == 4
	a = tree_predecessor (n4)
	assert a.key () == 6	

@pytest.mark.skip
def test_tree_insert (atree):
	A = []
	B = []
	x = Node (19)
	tree_insert (atree['root'], x)
	inorder_tree_walk (atree['root'], A)

	assert A[10] == x.key ()
	assert A[9] == 18
	assert A[11] == 20

	anotherroot = Node (3)
	tree_insert (anotherroot, x)
	inorder_tree_walk (anotherroot, B)

	assert B[0] == 3
	assert B[1] == x.key ()	

@pytest.mark.skip
def test_tree_insert2 (atree):
	A = []
	B = []
	x = Node (19)

	tree_insert2 (atree, x)
	inorder_tree_walk (atree['root'], A)

	assert A[10] == x.key ()
	assert A[9] == 18
	assert A[11] == 20

	anothertree = {'root': None}
	tree_insert2 (anothertree, x)
	inorder_tree_walk (anothertree['root'], B)

	assert len (B) == 1
	assert B[0] == x.key ()	

@pytest.mark.skip
def test_transplant (atree):
	v = Node (19)
	u = tree_search (atree['root'], 18)
	top = u.top ()
	transplant (atree, u, v)

	assert v.top () == top
	assert top.left () == v or top.right () == v

@pytest.mark.skip
def test_tree_delete (atree):
	A = []
	u = tree_search (atree['root'], 6)
	tree_delete (atree, u)
	v = tree_search (atree['root'], 7)
	e = [2,3,4,7,9,13,15,17,18,20]
	inorder_tree_walk (atree['root'], A)

	assert len (e) == len (A)
	for i in range (len (A)):
		assert e[i] == A[i]

	assert u.top () == v.top ()
	assert u.left () == v.left ()
	assert u.right () == v.right ()
