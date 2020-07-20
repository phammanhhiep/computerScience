import logging
import pytest

from binarySearchTrees_12.binarySearchTree import BinarySearchTree
from elementaryDataStructures_10 import linkedlist


logging.basicConfig(filename="log/test_binarySearchTree", level=logging.DEBUG)


@pytest.mark.skip
def test_inode_tree_walk():
    nodes = [linkedlist.Node(i) for i in range(1,11)]
    root = nodes[4]
    root.set_relative(1, nodes[1])
    root.set_relative(2, nodes[7])
    nodes[1].set_relative(1, nodes[0])
    nodes[1].set_relative(2, nodes[3])
    nodes[1].set_relative(3, root)
    nodes[7].set_relative(1, nodes[6])
    nodes[7].set_relative(3, root)
    nodes[0].set_relative(3, nodes[1])
    nodes[3].set_relative(3, nodes[1])
    nodes[6].set_relative(3, nodes[7])

    tree = BinarySearchTree(root)

    result = tree.inode_tree_walk()

    exp_result = [1,2,4,5,7,8]
    for i,j in zip(result, exp_result):
        assert i == j


@pytest.mark.skip
def test_inode_tree_walk2():
    nodes = [linkedlist.Node(i) for i in range(1,11)]
    root = nodes[4]
    root.set_relative(1, nodes[1])
    root.set_relative(2, nodes[7])
    nodes[1].set_relative(1, nodes[0])
    nodes[1].set_relative(2, nodes[3])
    nodes[1].set_relative(3, root)
    nodes[7].set_relative(1, nodes[6])
    nodes[7].set_relative(3, root)
    nodes[0].set_relative(3, nodes[1])
    nodes[3].set_relative(3, nodes[1])
    nodes[6].set_relative(3, nodes[7])

    tree = BinarySearchTree(root)

    result = tree.inode_tree_walk2()
    exp_result = [1,2,4,5,7,8]

    for i,j in zip(result, exp_result):
        assert i == j


def test_insert():
    nodes = [linkedlist.Node(i) for i in range(1,11)]
    root = nodes[4]
    root.set_relative(1, nodes[1])
    root.set_relative(2, nodes[7])
    nodes[1].set_relative(1, nodes[0])
    nodes[1].set_relative(2, nodes[3])
    nodes[1].set_relative(3, root)
    nodes[7].set_relative(1, nodes[6])
    nodes[7].set_relative(3, root)
    nodes[0].set_relative(3, nodes[1])
    nodes[3].set_relative(3, nodes[1])
    nodes[6].set_relative(3, nodes[7])


    tree1 = BinarySearchTree(None)
    tree1.insert(nodes[0])

    assert tree1.root_node.key == nodes[0].key

    tree2 = BinarySearchTree(root)
    tree2.insert(nodes[5])

    assert nodes[5].get_parent().key == nodes[6].key
    assert nodes[6].get_left().key == nodes[5].key

    exp_result = [1,2,4,5,6,7,8]
    result = tree2.inode_tree_walk2()

    for i,j in zip(result, exp_result):
        assert i == j
