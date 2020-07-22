import logging

import pytest

from redBlackTrees_13.redBlackTree import RedBlackTree, Node


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


@pytest.fixture
def aTree():
	tree = [Node(i) for i in range(10)]
	root = tree[5]
	root.set_left(tree[3])
	root.set_right(tree[7])
	tree[3].set_parent(root)
	tree[3].set_left(tree[1])
	tree[3].set_right(tree[4])
	tree[1].set_parent(tree[3])
	tree[1].set_right(tree[2])
	tree[2].set_parent(tree[1])
	tree[4].set_parent(tree[3])
	tree[7].set_parent(root)
	tree[7].set_left(tree[6])
	tree[7].set_right(tree[9])
	tree[6].set_parent(tree[7])
	tree[9].set_parent(tree[7])
	tree[9].set_left(tree[8])
	tree[8].set_parent(tree[9])	

	return tree


@pytest.mark.skip
def test_right_rotate(aTree):
	rb = RedBlackTree(aTree[5])
	node = aTree[3]
	parent = node.get_parent()
	left = node.get_left()
	right_child_of_left = left.get_right()
	rb.right_rotate(node)

	assert left.equal_to(parent.get_left())
	assert left.has_right_as(node)
	assert node.has_left_as(right_child_of_left)
	assert left.has_parent_as(parent)


@pytest.mark.skip
def test_left_rotate(aTree):
	rb = RedBlackTree(aTree[5])
	node = aTree[7]
	parent = node.get_parent()
	right = node.get_right()
	left_child_of_right = right.get_left()	
	rb.left_rotate(node)

	assert right.equal_to(parent.get_right())
	assert right.has_left_as(node)
	assert node.has_right_as(left_child_of_right)
	assert right.has_parent_as(parent)


@pytest.mark.skip
def test_delete_fixup():
	logging.debug("When x is the left child: Test case 1 and case 2")
	tree = [Node(i) for i in range(10)]
	root = tree[3]
	root.set_left(tree[2])
	root.set_right(tree[7])
	tree[2].set_parent(root)
	tree[7].set_parent(root)
	tree[7].set_red()
	tree[7].set_left(tree[5])
	tree[7].set_right(tree[8])
	tree[8].set_parent(tree[7])
	tree[5].set_parent(tree[7])
	tree[5].set_left(tree[4])
	tree[5].set_right(tree[6])
	tree[4].set_parent(tree[5])
	tree[6].set_parent(tree[5])


	rb = RedBlackTree(root)
	rb.delete_fixup(tree[2])

	assert rb.root_node.equal_to(tree[7])
	assert rb.root_node.is_black()
	assert rb.root_node.has_right_as(tree[8])
	assert tree[8].is_black()
	assert rb.root_node.has_left_as(tree[3])
	assert tree[3].is_black()
	assert tree[3].has_left_as(tree[2])
	assert tree[2].is_black()
	assert tree[3].has_right_as(tree[5])
	assert not tree[5].is_black()
	assert tree[5].has_left_as(tree[4])
	assert tree[5].has_right_as(tree[6])
	assert tree[4].is_black()
	assert tree[6].is_black()


@pytest.mark.skip
def test_delete_fixup2():
	logging.debug("When x is the left child: Test case 1, case 3, and 4")
	tree = [Node(i) for i in range(10)]
	root = tree[3]
	root.set_left(tree[2])
	root.set_right(tree[7])
	tree[2].set_parent(root)
	tree[7].set_parent(root)
	tree[7].set_red()
	tree[7].set_left(tree[5])
	tree[7].set_right(tree[8])
	tree[8].set_parent(tree[7])
	tree[5].set_parent(tree[7])
	tree[5].set_left(tree[4])
	tree[5].set_right(tree[6])
	tree[4].set_parent(tree[5])
	tree[4].set_red()
	tree[6].set_parent(tree[5])


	rb = RedBlackTree(root)
	rb.delete_fixup(tree[2])

	assert rb.root_node.equal_to(tree[7])
	assert rb.root_node.is_black()
	assert rb.root_node.has_right_as(tree[8])
	assert tree[8].is_black()
	assert rb.root_node.has_left_as(tree[4])
	assert not tree[4].is_black()
	assert tree[4].has_left_as(tree[3])
	assert tree[3].is_black()
	assert tree[3].has_left_as(tree[2])
	assert tree[2].is_black()
	assert tree[4].has_right_as(tree[5])
	assert tree[5].is_black()
	assert tree[5].has_right_as(tree[6])
	assert tree[6].is_black()


@pytest.mark.skip
def test_delete_fixup3():
	logging.debug("When x is the right child: Test case 1 and case 2")
	tree = [Node(i) for i in range(10)]
	root = tree[6]
	root.set_right(tree[7])
	root.set_left(tree[2])
	tree[2].set_parent(root)
	tree[7].set_parent(root)
	tree[2].set_red()
	tree[2].set_left(tree[1])
	tree[1].set_parent(tree[2])
	tree[2].set_right(tree[5])
	tree[5].set_parent(tree[2])
	tree[5].set_left(tree[3])
	tree[5].set_right(tree[4])
	tree[3].set_parent(tree[5])
	tree[4].set_parent(tree[5])
	
	

	rb = RedBlackTree(root)
	rb.delete_fixup(tree[7])

	assert rb.root_node.equal_to(tree[2])
	assert rb.root_node.is_black()
	assert rb.root_node.has_right_as(tree[6])
	assert tree[6].is_black()
	assert rb.root_node.has_left_as(tree[1])
	assert tree[1].is_black()
	assert tree[6].has_left_as(tree[5])
	assert tree[6].is_black()
	assert tree[6].has_right_as(tree[7])
	assert not tree[5].is_black()
	assert tree[5].has_left_as(tree[3])
	assert tree[5].has_right_as(tree[4])
	assert tree[4].is_black()
	assert tree[6].is_black()


@pytest.mark.skip
def test_delete_fixup4():
	logging.debug("When x is the right child: Test case 1, and case 3 and 4")
	tree = [Node(i) for i in range(10)]
	root = tree[6]
	root.set_right(tree[7])
	root.set_left(tree[2])
	tree[2].set_parent(root)
	tree[7].set_parent(root)
	tree[2].set_red()
	tree[2].set_left(tree[1])
	tree[1].set_parent(tree[2])
	tree[2].set_right(tree[5])
	tree[5].set_parent(tree[2])
	tree[5].set_left(tree[3])
	tree[5].set_right(tree[4])
	tree[3].set_parent(tree[5])
	tree[4].set_parent(tree[5])
	tree[4].set_red()
	

	rb = RedBlackTree(root)
	rb.delete_fixup(tree[7])

	assert rb.root_node.equal_to(tree[2])
	assert rb.root_node.is_black()
	assert rb.root_node.has_right_as(tree[4])
	assert not tree[4].is_black()
	assert rb.root_node.has_left_as(tree[1])
	assert tree[1].is_black()
	assert tree[4].has_right_as(tree[6])
	assert tree[6].is_black()
	assert tree[6].has_right_as(tree[7])
	assert tree[4].has_left_as(tree[5])
	assert tree[5].is_black()
	assert tree[5].has_left_as(tree[3])
	assert tree[3].is_black()
	assert tree[7].is_black()