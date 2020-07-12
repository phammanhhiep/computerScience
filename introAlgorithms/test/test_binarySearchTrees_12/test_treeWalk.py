import logging
import pytest

from binarySearchTrees_12.treeWalk import inoderTreeWalk1
from elementaryDataStructures_10 import linkedlist


logging.basicConfig(filename="log/test_inorderTreeWalk", level=logging.DEBUG)

def test_inoderTreeWalk1():
    nodes = [linkedlist.Node(i) for i in range(1,11)]
    root = nodes[4]
    root.set_relative(1, nodes[1])
    root.set_relative(2, nodes[5])
    nodes[1].set_relative(1, nodes[0])
    nodes[1].set_relative(2, nodes[3])
    nodes[1].set_relative(3, root)
    nodes[5].set_relative(1, nodes[2])
    nodes[5].set_relative(3, root)
    nodes[0].set_relative(3, nodes[1])
    nodes[3].set_relative(3, nodes[1])
    nodes[2].set_relative(3, nodes[5])

    result = inoderTreeWalk1(root)

    exp_result = [1,2,4,5,3,6]
    for i,j in zip(result, exp_result):
        assert i == j