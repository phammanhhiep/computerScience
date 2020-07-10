import os, sys
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from trees.augmentedRedBlackTree import Node2 as Node, os_select, os_rank

@pytest.fixture
def atree ():
	root = Node (key=26, size=20)
	n1 = Node (key=17, size=12, top=root)
	n2 = Node (key=41, size=7, top=root)
	n3 = Node (key=14, size=7, top=n1)
	n4 = Node (key=21, size=4, top=n1)
	n5 = Node (key=30, size=5, top=n2)
	n6 = Node (key=47, size=1, top=n2)
	n7 = Node ()
	n8 = Node ()
	n9 = Node ()
	n10 = Node ()
	n11 = Node (key=28, size=1, top=n5)
	n12 = Node (key=38, size=3, top=n5)
	n13 = Node ()
	n14	= Node ()
	n15 = Node ()
	n16 = Node ()
	n17 = Node (key=35, size=1, top=n12)
	n18 = Node (key=39, size=1, top=n12)
	n19 = Node (key=3, size=1)

	root._left = n1
	root._right = n2
	n1._left = n3
	n1._right = n4
	n2._left = n5
	n2._right = n6
	n5._left = n11
	n5._right = n12
	n12._left = n17
	n12._right = n18

	T = {}
	T['root'] = root
	return T

@pytest.mark.skip
def test_os_select (atree):
	n = os_select (atree['root'], 17)
	assert n.key () == 38

@pytest.mark.skip
def test_os_rank (atree):
	n = os_select (atree['root'], 17) 
	i = os_rank (atree['root'], n)

	assert i == 17