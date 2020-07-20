import logging

import pytest

from redBlackTrees_13.redBlackTree import RedBlackTree, Node


logging.basicConfig(filename="redBlackTree.log", level=logging.DEBUG)


@pytest.fixture
def aTree():
	tree = [Node(i) for i in range(10)]
	root = tree[5]
	root.set_left(tree[3])
	root.set_right(tree[7])
	tree[3].set_parent(root)
	tree[3].set_left(tree[2])
	tree[3].set_right(tree[4])
	tree[2].set_parent(tree[3])
	tree[4].set_parent(tree[3])
	tree[7].set_parent(root)
	tree[7].set_left(tree[6])
	tree[7].set_right(tree[8])
	tree[6].set_parent(tree[7])
	tree[8].set_parent(tree[7])	

	return tree


@pytest.mark.skip
def test_right_rotate(aTree):
	rb = RedBlackTree(aTree[5])
	rb.right_rotate(rb.root_node)

	assert rb.root_node.get_key() == 3
	assert rb.root_node.get_left().get_key() == 2
	assert rb.root_node.get_right().get_key() == 5
	assert rb.root_node.get_right().get_left().get_key() == 4


# @pytest.mark.skip
def test_left_rotate(aTree):
	rb = RedBlackTree(aTree[5])
	rb.left_rotate(rb.root_node)

	assert rb.root_node.get_key() == 7
	assert rb.root_node.get_left().get_key() == 5
	assert rb.root_node.get_right().get_key() == 8
	assert rb.root_node.get_left().get_right().get_key() == 6	